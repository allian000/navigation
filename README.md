# 室內導航

## 概述
根據起點與終點算出最短距離並繪製地圖。

## 地圖檔資料集

### 命名規則

| 檔案名稱  | 說明                                |
|----------|------------------------------------|
| set_$    | 組合 ID，代表顯示地圖和可用路徑的組合    |
| map      | 提供給使用者顯示最短路徑的地圖圖像       |
| path     | 提供程序計算最短路徑的路徑圖像          |

### 範例

以下是圖像檔案範例:
```text
set_1_map.png
set_1_path.png
```

## 類別說明

### `Point` 類別

表示地圖上的關鍵點（交叉點、轉角點或死路），包含以下屬性：

- `x`: X 座標
- `y`: Y 座標
- `point_type`: 點的類型（`'intersection'`，`'turn'`，`'dead_end'`）

### `ImageProcessor` 類別

負責圖像處理，包括：

- `load_image(image_id: str)`: 加載圖像檔案
- `find_available_points(image)`: 在圖像中查找所有關鍵點

### `PathFinder` 類別

負責建立圖形結構和尋找最短路徑，包括：

- `build_graph(points)`: 根據關鍵點建立加權圖
- `find_shortest_path(start_point, end_point, points)`: 使用 Dijkstra 算法找到最短路徑

## 功能說明

### 加載圖像

`load_image(image_id: str)`：加載指定 ID 的地圖圖像。

### 查找關鍵點

`find_available_points(image)`：在圖像中查找符合條件的關鍵點，並將其分類為交叉點、轉角點或死路。

### 繪製最短路徑

`draw_shortest_path(image, path, map_id: str, output_path='shortest_path.png')`：在圖像上繪製最短路徑並保存結果。

### 可視化關鍵點

`visualize_key_points(image, points, output_path='key_points.png')`：將關鍵點標記在圖像上，並保存結果。

## 範例程式碼

以下是使用本系統的範例程式碼：

```python
if __name__ == '__main__':
    image_processor = ImageProcessor()
    path_finder = PathFinder()

    # 加載地圖圖像
    image = image_processor.load_image('1')

    # 查找所有關鍵點
    available_points = image_processor.find_available_points(image)

    # 建立圖形結構
    path_finder.build_graph(available_points)

    # 定義起點和終點
    start_point = (525, 677)  # 起點座標
    end_point = (709, 337)    # 終點座標

    # 查找最短路徑
    shortest_path = path_finder.find_shortest_path(start_point, end_point, available_points)

    # 繪製最短路徑
    if shortest_path:
        draw_shortest_path(image, shortest_path, '1', 'shortest_path.png')

    # 可視化關鍵點
    visualize_key_points(image, available_points)
```

## 測試案例

```python
class TestCase:
    """
    測試案例類別，存儲圖像 ID、起點和終點
    """
    def __init__(self, image_id, start, end):
        self.image_id = image_id
        self.start = start
        self.end = end

def load_test_cases():
    test_cases = [
        TestCase('1', (525, 677), (709, 337)),
        # 可以添加更多測試案例
    ]
    return test_cases

```