import math
import networkx as nx
from PIL import Image, ImageDraw


# 單一職責的 Point 類
class Point:
    def __init__(self, x, y, point_type):
        self.x = x
        self.y = y
        self.point_type = point_type  # 'intersection', 'turn', 'dead_end'

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.point_type})"


class ImageProcessor:
    """
    圖像處理類，負責載入圖片和查找可用點。
    """

    TARGET_COLOR = (45, 225, 218)

    @staticmethod
    def load_image(image_id: str):
        image = Image.open(f'./maps/set_{image_id}_path.png')
        image = image.convert('RGB')
        return image

    def find_available_points(self, image):
        """
        找出圖片中的所有可用點
        """
        width, height = image.size
        points = []
        for y in range(height):
            for x in range(width):
                pixel_color = image.getpixel((x, y))
                if pixel_color == self.TARGET_COLOR:
                    point_type = self.is_key_point(image, x, y)
                    if point_type:
                        points.append(Point(x, y, point_type))
        return points

    @staticmethod
    def is_key_point(image, x, y):
        """
        判斷一個點是否為關鍵點（交叉、轉角或死路）
        """
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 上下左右
        directions = set()

        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if 0 <= nx < image.width and 0 <= ny < image.height:
                if image.getpixel((nx, ny)) == ImageProcessor.TARGET_COLOR:
                    directions.add((dx, dy))

        num_directions = len(directions)

        if num_directions > 2:
            return 'intersection'
        elif num_directions == 2:
            dirs = list(directions)
            if (dirs[0][0] == -dirs[1][0] and dirs[0][1] == -dirs[1][1]):
                return None  # 直線
            return 'turn'  # 轉角
        elif num_directions == 1:
            return 'dead_end'  # 死路
        return None


class PathFinder:
    """
    負責根據點構建圖並尋找最短路徑的類
    """

    def __init__(self):
        self.graph = None

    def build_graph(self, points):
        """
        根據點構建加權圖
        """
        G = nx.Graph()
        for i, point in enumerate(points):
            G.add_node(i, point=point)

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                if p1.x == p2.x or p1.y == p2.y:  # 僅考慮水平或垂直
                    distance = euclidean_distance(p1, p2)
                    G.add_edge(i, j, weight=distance)
        self.graph = G

    def find_shortest_path(self, start_point, end_point, points):
        """
        使用 Dijkstra 尋找兩點之間的最短路徑
        """
        start_idx = next(i for i, p in enumerate(
            points) if (p.x, p.y) == start_point)
        end_idx = next(i for i, p in enumerate(
            points) if (p.x, p.y) == end_point)
        path = nx.dijkstra_path(self.graph, start_idx,
                                end_idx, weight='weight')
        return [points[i] for i in path]


# 輔助函數：計算兩點間距離
def euclidean_distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


def draw_shortest_path(image, path, map_id: str, output_path='shortest_path.png'):
    """
    在圖片上繪製最短路徑，並保存結果。
    """
    draw = ImageDraw.Draw(image)
    for i in range(len(path) - 1):
        p1 = (path[i].x, path[i].y)
        p2 = (path[i + 1].x, path[i + 1].y)
        draw.line([p1, p2], fill="red", width=2)
    image.save(f"./outputs/set_{map_id}_{output_path}")
    image.show()


# 測試案例基礎架構
class TestCase:
    """
    測試案例類，儲存起點和終點等信息
    """

    def __init__(self, image_id, start, end):
        self.image_id = image_id
        self.start = start
        self.end = end


def load_test_cases():
    """
    載入測試案例
    """
    return [
        TestCase(1, (525, 677), (709, 337))
    ]


if __name__ == '__main__':
    # 測試過程
    image_processor = ImageProcessor()
    path_finder = PathFinder()

    test_cases = load_test_cases()
    for case in test_cases:
        image = image_processor.load_image(case.image_id)
        available_points = image_processor.find_available_points(image)

        path_finder.build_graph(available_points)
        shortest_path = path_finder.find_shortest_path(
            case.start, case.end, available_points)

        if shortest_path:
            draw_shortest_path(image, shortest_path, case.image_id, 'shortest_path.png')
