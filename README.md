![logo](assets/logoMicro.png)

## Main

 * Name: RMG (rouge map creator)
 * Author: KseandI
 * Version: 0.0.1
 * Made: with love and for Liqerty Team
 * Logo: I know the logo is bad

---

## Usage

##### create map

```python
# Create map with size (x, y)
# wall - char of wall | air - char of air
createMap(x: int, y: int, wall: str = "#", air: str = "*") -> list
# map[x][y] is string

# Example:
map = createMap(10, 10, "#", "*")
# Will create map 10x10
```

##### add rectangle

```Python
# Return grid: list with rect in pos (x, y) and with width and height (w, h)
# stroke - char of borders
rect(grid: list, x: int, y: int, w: int, h: int, stroke: str = "#") -> list

# Example:
map = rect(map, 2, 2, 3, 3, "W")
# Create rect on map with coords x=2, y=2 and with size w and h. Borders will be "W"
```

---

### About

[Github](http://https://github.com/KseandI) | [Email](KseandI@gmail.com) | [Reddit](https://www.reddit.com/user/KseandI) | [VK](https://vk.com/xxigor2005xx)
