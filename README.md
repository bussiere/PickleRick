

```python
#first we pickle Rick 
import pickle

rick = """
class Rick:  # Définition de notre classe Personne
    def __init__(self):  # Notre méthode constructeur
        print("Pickle Riiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiick")
        self.name = "Sanchez"
        self.pic = "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"
rick = Rick()
"""
with open('Rick', 'wb') as f:
    pickle.dump(rick,f)
```


```python
#then we load him with pickle and cheat with exec :
import pickle

with open('Rick', 'rb') as f:
    exec(pickle.load(f))

print(rick.name)
```

    Pickle Riiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiick
    Sanchez


#so we have a pickle Rick now ...
#source here

https://github.com/bussiere/PickleRick


```python
from IPython.display import display, HTML
display(HTML('''<img src="data:image/png;base64,'''+rick.pic+'''">'''))
```


<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAKL2lDQ1BJQ0MgcHJvZmlsZQAASMedlndUVNcWh8+9d3qhzTDSGXqTLjCA9C4gHQRRGGYGGMoAwwxNbIioQEQREQFFkKCAAaOhSKyIYiEoqGAPSBBQYjCKqKhkRtZKfHl57+Xl98e939pn73P32XuftS4AJE8fLi8FlgIgmSfgB3o401eFR9Cx/QAGeIABpgAwWempvkHuwUAkLzcXerrICfyL3gwBSPy+ZejpT6eD/0/SrFS+AADIX8TmbE46S8T5Ik7KFKSK7TMipsYkihlGiZkvSlDEcmKOW+Sln30W2VHM7GQeW8TinFPZyWwx94h4e4aQI2LER8QFGVxOpohvi1gzSZjMFfFbcWwyh5kOAIoktgs4rHgRm4iYxA8OdBHxcgBwpLgvOOYLFnCyBOJDuaSkZvO5cfECui5Lj25qbc2ge3IykzgCgaE/k5XI5LPpLinJqUxeNgCLZ/4sGXFt6aIiW5paW1oamhmZflGo/7r4NyXu7SK9CvjcM4jW94ftr/xS6gBgzIpqs+sPW8x+ADq2AiB3/w+b5iEAJEV9a7/xxXlo4nmJFwhSbYyNMzMzjbgclpG4oL/rfzr8DX3xPSPxdr+Xh+7KiWUKkwR0cd1YKUkpQj49PZXJ4tAN/zzE/zjwr/NYGsiJ5fA5PFFEqGjKuLw4Ubt5bK6Am8Kjc3n/qYn/MOxPWpxrkSj1nwA1yghI3aAC5Oc+gKIQARJ5UNz13/vmgw8F4psXpjqxOPefBf37rnCJ+JHOjfsc5xIYTGcJ+RmLa+JrCdCAACQBFcgDFaABdIEhMANWwBY4AjewAviBYBAO1gIWiAfJgA8yQS7YDApAEdgF9oJKUAPqQSNoASdABzgNLoDL4Dq4Ce6AB2AEjIPnYAa8AfMQBGEhMkSB5CFVSAsygMwgBmQPuUE+UCAUDkVDcRAPEkK50BaoCCqFKqFaqBH6FjoFXYCuQgPQPWgUmoJ+hd7DCEyCqbAyrA0bwwzYCfaGg+E1cBycBufA+fBOuAKug4/B7fAF+Dp8Bx6Bn8OzCECICA1RQwwRBuKC+CERSCzCRzYghUg5Uoe0IF1IL3ILGUGmkXcoDIqCoqMMUbYoT1QIioVKQ21AFaMqUUdR7age1C3UKGoG9QlNRiuhDdA2aC/0KnQcOhNdgC5HN6Db0JfQd9Dj6DcYDIaG0cFYYTwx4ZgEzDpMMeYAphVzHjOAGcPMYrFYeawB1g7rh2ViBdgC7H7sMew57CB2HPsWR8Sp4sxw7rgIHA+XhyvHNeHO4gZxE7h5vBReC2+D98Oz8dn4Enw9vgt/Az+OnydIE3QIdoRgQgJhM6GC0EK4RHhIeEUkEtWJ1sQAIpe4iVhBPE68QhwlviPJkPRJLqRIkpC0k3SEdJ50j/SKTCZrkx3JEWQBeSe5kXyR/Jj8VoIiYSThJcGW2ChRJdEuMSjxQhIvqSXpJLlWMkeyXPKk5A3JaSm8lLaUixRTaoNUldQpqWGpWWmKtKm0n3SydLF0k/RV6UkZrIy2jJsMWyZf5rDMRZkxCkLRoLhQWJQtlHrKJco4FUPVoXpRE6hF1G+o/dQZWRnZZbKhslmyVbJnZEdoCE2b5kVLopXQTtCGaO+XKC9xWsJZsmNJy5LBJXNyinKOchy5QrlWuTty7+Xp8m7yifK75TvkHymgFPQVAhQyFQ4qXFKYVqQq2iqyFAsVTyjeV4KV9JUCldYpHVbqU5pVVlH2UE5V3q98UXlahabiqJKgUqZyVmVKlaJqr8pVLVM9p/qMLkt3oifRK+g99Bk1JTVPNaFarVq/2ry6jnqIep56q/ojDYIGQyNWo0yjW2NGU1XTVzNXs1nzvhZei6EVr7VPq1drTltHO0x7m3aH9qSOnI6XTo5Os85DXbKug26abp3ubT2MHkMvUe+A3k19WN9CP16/Sv+GAWxgacA1OGAwsBS91Hopb2nd0mFDkqGTYYZhs+GoEc3IxyjPqMPohbGmcYTxbuNe408mFiZJJvUmD0xlTFeY5pl2mf5qpm/GMqsyu21ONnc332jeaf5ymcEyzrKDy+5aUCx8LbZZdFt8tLSy5Fu2WE5ZaVpFW1VbDTOoDH9GMeOKNdra2Xqj9WnrdzaWNgKbEza/2BraJto22U4u11nOWV6/fMxO3Y5pV2s3Yk+3j7Y/ZD/ioObAdKhzeOKo4ch2bHCccNJzSnA65vTC2cSZ79zmPOdi47Le5bwr4urhWuja7ybjFuJW6fbYXd09zr3ZfcbDwmOdx3lPtKe3527PYS9lL5ZXo9fMCqsV61f0eJO8g7wrvZ/46Pvwfbp8Yd8Vvnt8H67UWslb2eEH/Lz89vg98tfxT/P/PgAT4B9QFfA00DQwN7A3iBIUFdQU9CbYObgk+EGIbogwpDtUMjQytDF0Lsw1rDRsZJXxqvWrrocrhHPDOyOwEaERDRGzq91W7109HmkRWRA5tEZnTdaaq2sV1iatPRMlGcWMOhmNjg6Lbor+wPRj1jFnY7xiqmNmWC6sfaznbEd2GXuKY8cp5UzE2sWWxk7G2cXtiZuKd4gvj5/munAruS8TPBNqEuYS/RKPJC4khSW1JuOSo5NP8WR4ibyeFJWUrJSBVIPUgtSRNJu0vWkzfG9+QzqUvia9U0AV/Uz1CXWFW4WjGfYZVRlvM0MzT2ZJZ/Gy+rL1s3dkT+S453y9DrWOta47Vy13c+7oeqf1tRugDTEbujdqbMzfOL7JY9PRzYTNiZt/yDPJK817vSVsS1e+cv6m/LGtHlubCyQK+AXD22y31WxHbedu799hvmP/jk+F7MJrRSZF5UUfilnF174y/ariq4WdsTv7SyxLDu7C7OLtGtrtsPtoqXRpTunYHt897WX0ssKy13uj9l4tX1Zes4+wT7hvpMKnonO/5v5d+z9UxlfeqXKuaq1Wqt5RPXeAfWDwoOPBlhrlmqKa94e4h+7WetS212nXlR/GHM44/LQ+tL73a8bXjQ0KDUUNH4/wjowcDTza02jV2Nik1FTSDDcLm6eORR67+Y3rN50thi21rbTWouPguPD4s2+jvx064X2i+yTjZMt3Wt9Vt1HaCtuh9uz2mY74jpHO8M6BUytOdXfZdrV9b/T9kdNqp6vOyJ4pOUs4m3924VzOudnzqeenL8RdGOuO6n5wcdXF2z0BPf2XvC9duex++WKvU++5K3ZXTl+1uXrqGuNax3XL6+19Fn1tP1j80NZv2d9+w+pG503rm10DywfODjoMXrjleuvyba/b1++svDMwFDJ0dzhyeOQu++7kvaR7L+9n3J9/sOkh+mHhI6lH5Y+VHtf9qPdj64jlyJlR19G+J0FPHoyxxp7/lP7Th/H8p+Sn5ROqE42TZpOnp9ynbj5b/Wz8eerz+emCn6V/rn6h++K7Xxx/6ZtZNTP+kv9y4dfiV/Kvjrxe9rp71n/28ZvkN/NzhW/l3x59x3jX+z7s/cR85gfsh4qPeh+7Pnl/eriQvLDwG/eE8/vMO7xsAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4QgOAwwdDJbD+QAAGHVJREFUeNrtnXmUXXWV7z/7d865Q926Nc9JJUAMSYAQCAKGECBAowIKKrQKNgpKg/rwiTbP5dPu91TU1zwnlMZFg7aCPhzABkFBAy1zEEgCAgESCJkqlZrr1nCnM+z3x7m3MtWcVOa9VrJWrbp17jn7+9vT97d/+wiHpShlYF9cVmVdXDun5Ei7RFrWP9f361y/d9fevAk5jAP/1Hhc8vN1s+PT6o4oJVFvqbqIImrZKu1r0nS35n/x2sMdXwfWHgZk6uSC2iMTvzvx0vpI48wSLS9zZDCdp3Ori7HA9xQEVMEYUTfjS8vqvmdfur/jiqkE5hAFxPzkpA/WX9X8zqTmBgO5+KONqIIIRGMWa1YP8PKKXsSAAoKgKIJobtCTjatSt762rPuzhwHZTZm/sNpa+3rf1qVfmFHjOIYggHMvqCYWdzAGfBeefqyL7u48pqAZEQEUEUEBUGzbouPtwfan7ti8EGg5DMgkzSJRGc2c84XmiPqCAMecUMbsuSW0t3msXdNPe0ueRIkhVmLhRAQRwXMDUj0unqvbaUtBRTN9njz9s9bj0t3ZVw8DMkGJRiNd5335iCohVKwAPgFvPxUwd9ZZlMZryfotbGl/nkRdH+94Vy35waKGhLYtGVSH4EBUCUBzOVee/kHb0elMdu1hQMZvHCsv+MoRJxrHAlGEcPW3PlrJrb9aTjrv4rtZ8nkhGnd4+7XVPPqHX/B2z90c/+5afBfSAy6pXh/ZXmMKIDrYk8s9evOGMsA9DMjYT/jB0z857d6q5pJihIZCiG59JU1ppILBbDvxaAWJWBVl8VnMmnkuS9//AQb7evnOjR9h3vtSGHFobclud40iKApitG1t/wN//UXrRYcBGUOqj0p4iz/eZApJ1NDKjsSF6pooqqAaBm0RwYka+roGWfuUyzmnfoV3X3oF3/7SFdSf8SL9KcjnfHY0kwLABp7/acc5W99O/ddu2fJBjsfDiz7WaCkqYaYERHwCy6VhRowg0CEwwsUekMt4xBJR5r+7jDXuN7n9uzfwpW/9nLf/MINYwhQyrV3XtfiizYsT/7bbzvXg9VRS9c6PNJ1nbFHBEIlZbFjus8j8AxfP/CLxv53JK8s6caIUgnWh4hChWBGWVyfxZzzAY3+8m69+77dsWZEb2akIUtUcnQuUHwZkuAezrDVNcxNCoGJHhf4n63jyj8u48oYPceHHzuKGb13Ng3c/Rt8T88hmcqhKMUpvc+ZGKSlPcO+D19PXm6LR+RDgj2AlEE9GaJhXsuQwILus1sgFZ/y3adVBIWV94Zfd/PL+2xgM0tt8voKHyy2334jz4rvw3WCbpYSBBVFAhCUfn8HyR37N+z5xNe3rBxjKf3eSwFdmLEzOPwzITlKSkN+XVjpqALsEbvveLQTiY1CWL3uRVFv/ULaU0zy3/eTbdLzhDbkrsawwcEtYQLoDAc+8/gMe/9192BFrZLcVBNiOs2B37t0++GKH/eUzrmsyIoKq4qkyd/5slDDPuu6qf+HpV3+3w9+kSOH2xGl9s5P85kri8VIGst2kpYPjltaBb3PsWTUE8jOqNpWGljOMaGCwI3L0YUC2k4oG55vRuK1BgCBgWzaeWwwPyopNDwzVIcV17mCzfmWKH37qR5y+5ERcckSI0plKcde/38ejb/2E2e+qZCBVcGcyvIWIKFhU7s79WwcTGBb2b869oflYVSlwgkJFlQ0tNcxdcFRBkQoqSIFaF5QVT7zBpR/9APNOmUmePJ76ZDWPHYMTTpvHvKrFLFv+nwTGwg9GKd5EyXnas+HZ1M2HYwjQtKDkkgBRkbC+qKi0WXZzKz+6+0Y07YRua4jzUESUUlPB//nGD5h7wpGFYK+oKMYIqoJBOH7xkVib3oGPIiPmWKAIlh6uQ4qP8sJJH24SS4yAUDctRml5hLP/sZaFH6jjgsvO4vlHVpOUMhzjEJEI+T7lfR95N5+9/hO4GtYYguAOBNx+093YJnQgnionH3c62YzLKHggquQG/d1iPw6KGGKMvej0f2xY6Od99d1AWlf10V3l4Ps+ESdCqjvPMUvL+Y9nvsQtd5Uyc/ps2tal2MpqllzeSKIiWbAOAVHyuTw//uEvueZ/XDbEV0UTUegLUNsehW8S/HyQOuQtJFFtP1PREMcLPHl7RT8nf6iewA2wbZujz0iink/XuhxbVmdoXiL89YVnqD27nQXn1tHf5XPP3fdgix1mugiJqhgrNj+ApwGgGAPLly8nXhYZnfwzkM94Lx/SFmKwfrz0uukQICvv6uCcTzdy5xfXUloT8k7Vvady+uU2bjbAmAraN/Sx4PwqjLGwYoKb83nT/S82rfksjbPLC1YiEIRBWhWCQcMmVlCXLwkLxhGyLGOEwW7/pUPWQhwLe9aS5LWqohqDU66q575vbKKkWtAg/Ncwo5Zff3ETxgYl4NVHeomXOdgxePKnWwhcOPpd9Vzz1Ut45uG/UWpihAmaYkQgZ3P+xR+k4dgSBEYEQ1UJRHnjka7Hdq+OOrAT3XUXfXPWkYEbEPgu9c1l3PO1NTgxU1CS4OVcejdm+eBHL6Txgi08+6sWyhtK6OvMccolDQT5AGyFQGl9u59o65HMP2oJjdPreOO1Nfxx5a+Zc2YVgReMfisK3S1Znrp90yEb1Bec+emmIwIvQATshEOsBNTbvlALcOI2808+lkzKpXugkpMuqkdRjF2On/cL+yAWz92zhTlLKqla2kub3M/mdJ6BaTA7VhmCoWMsXxHSKe+x3X2oAxaQ0kpnVXl9VLSopTy89pdOxDVDLkREIFDa+jbw2P3P4Tg2X/nfN9Amq0jrAA3N1VQ0WlQ1lHDqhxtZvzLFhlUpBIOagLxrmH5CKUEwYnE+ZB5WROh6s+8/D01AxLr+rOtnQkChUBMcx/DGs2nO+dw0HrljA5GohWr4O1VYuHgB+YGAlo2bOPKoWWTSGaoqavjV3b/i49dezjtOK+WYs0s54p0VODHFzSktb2UJtLCxNZp5qJDuybNh5eD/2/0k5QCUGQuT3zOBKVhHqKho1PD+G5qxrYAZ5XOws0mMCSkSUSitiVB9ZJwZ85opbbI46dQToTzNv3zry+RkgMrcXO784lpe/lMH6hte+H0XMmR/o4cFFehYm30T6Nx9+ufAS3MfOvtzzbOiEUdyGQ9jhcpKJC0MhjVP9nHkuR7uxnoWv/Ms1m5YjZgw6IpCLGHju9De3klGA9L5bowNLe0biJYKbety9LXkyGQ9yuqjGNuMmfnYEcP653v/b29L7qlDDZDSUy5r/KktgWxa20Yk4uDELRRIljlYtlA3J8GKe3uonJXjf/3377JpXRutGzpQJ19Y6cJgSnmgopILnDhl/coq18WKmpABtpT29TlO+GAN3S1ZSssjoxuIKpneHCt+2/5poPuQclm2ba8++tQ67WxPYYxFSVVsyGcYC4JAET/g7KsbGejNc+13zueM086iedoRXHLeFYhrg0Cy2nB+XzfPpXMsLY9zk1NOPhsghebEWLmQ7vHI9fujBnMNW4DY8kq6C3hzz3iAA0fmLvnctGbfD4TAkKxJFJRihpQmhV0+Lx9w6iUNnHReEy+X/ph1W//Gzd/9PvkBWDjrNAJficV9bnVydOUDaqMWDanQgBQhcIVY3MJ2DBQ2ukZcJHGh5W+D/7rnXPIBklfFEpGVybIIA/0ZqqYnSVYXaYwA25adKugws1LANhE+/O2jOfPKmSw5dSl/fvgRch3KnTf/Fsvz+FNqABAqCqWGATI9PpkBn2SNQxAEw1bnxa74rW/009Oaue2QAkRse+E518+II4qiRBORgkbCmJBI2sPS4kKYYrlpn/nnNDLtkrdY8tGZXPyBi2iqb+Kqv/8MA6csospARCx8F7L9ytnXN9Hy4iDlDbFRKA4Fg7a/lvkz0LfHnvVAwKOioSRYcu00pED2bb9iFaWhKR5un44efYcsJ5Y0tLzey9a1GfDitG5OYUUtGmbGiVZZrH+6n2PeW1OwwJGvGAQBD35t3Vmgjx8yFmJsc+3pn5muRYXv4j4Ke+VhX9XYa09QsgMB1dOTzF9ajxWHeNLBiUJ3S4ZMl8/8C8cGA+DN5amOPQnGgVCpm/pZiVtlBO5CUWIxa0QGdiTOqdgSN9DvUnmUQ+28SvANnq+o7xP4OiZVYmzDur+k/mmPZ5L7NZdr2zedelWj+tmwN3d7l6Qooobyqiij7quOpFJf6e8LuxDdTIBIGNXHAldRUMOaJ7rJu+6dhxIg9uwlZV/0M8G2ftudXJVlFRQ5gVCoqhiBzvb8tngk44+oguCUCC0vD3xtapiI/VSciP37eX9Xp8Ov2NAiaurjyATTEhEh1evh+1pIBCZoWQqbX+ontSX7w0MJkKoTL615b+AFsmtRFgbwSMQUmtRlQsr0fRgc8MZmcEdMMkRbV/f/Zk/QJAcMINGE/VLTvKSOVJQJQlVNJGRjx61TxRilqz1X6FmcXMafS3uycVX/jVNHnu5vRYdlTjvn883TA3/kgxhIgLFkQtaBCgN9oatSmXQ3m771RM8bwMuHCiBW49zk03bE3uFk0y5B2cg4dvF2/BvVMKsqHvqcTPAwjsr6Z/uvm9I8f39CIxJ17jj1igYdDoxtscRQWTP+VFc17OVta80O8U8TxgJFxeiax3u7XM9bNqWp5X6Ex+xFn2z8hJcZPi4UjxfE4wbHGUdADjup8Tylqy0DmHHQKyM5SYNxRFpe7LtqynP9/aYin518vbw+qhDIcEpTVWxbqKiOjGdJgxEG+1z6Ut7QWAyZLHWnyhuPdmVTbfnfT7ki9gtXFbN/vPjqxkLqI8MudhBqG8Z2VUXX1tWWpy/lDU1imCyLqihWzLDhuYEr90pSsx8YxzFnfWbGq8k6u0CXD6+W6toYtiMjBvLi+UDX9enucPfcoym8+VRvZvUjHSV7RRv7mh6ZviD5almdo4XzNcO7KscUhsGMVoEr2YxPV7s7/IUmaR1O3NC6buATe2157ks0Sssj9516eb1GYo4MfzIpTFFr6iJjuqpcNqC320VkzxmHqLDu+RQ96zK/PegBsR3nvNOunXaBE0TkrZUtZHoz251w2kaR1DRECwXg6I1q3Z354UnI8aTFIynHETrXD36OydDJBxggiTnnVP4pGg/3MiwbSqriQ6oMCzmhutaheEJ5NMfS3pYh3A3UCTulbfXOrpxZqj3Dphf6f7ZXI+q+QKN+dunrs5dUqIgwmMlQf1Q1ljHbDYKxqKh0cCJm1P0JVcimlcDfWbljSwCIGHrb+sINq53jjli6YXn/T4H+gxqQeDL6/UWfbJrme+GcBRXBcswO3R3RKMQT1piuRgR6unNDheOEOBqBzo09pHszxGI7xyjFDzxZ91zvt/Z6zrk3v0zELFr0qcbP+9ltxV/x/+1nG1bVRUfksrZ3Nf0pb1IRXFXJDOTIpfOghmA7MFQVxejqh7teA97a67F1L35XxcIP1T5TWuEMy1+EW7JCdV2EwA/GcFWCiDLQ705qX0NEcIyhrKqUWNLBLZwTKf5OJJDNqwY/tk+Snb1lHLMXV745/fhyDYJAZJgBYGgY3J2IjEOhSj7HpK0DwMRskokQfN/3t7k9EX3p/rZX3Zy7cp+UyXvjSxrmJv9y/PsbqjQIZDQSo6omNnaKWxiL0ZfyJpyNWpY1NDlORNBAd/xZlWwqL+tX9H1gn/EWU/0F1TNK71t8ZdOZ+YxbOKwxwo1YoYWMFZu1ULC5eW/CgdzzvJ1qnR2vbEeMPn93+wPsocbp/Q6Qypklt59+TdNFbsYfMyaUl1vjqyMUAi124U7MQkRkWJpRC/Oz1q9MSc+W9BX7lNmbqgtXNca+dubV0z8VeCNv7Q35c6PEEva4eqJEhJ7O3ITbf0YFCsGJGd5Y1n0D0LsvAZkStrekOv7JpZ9pusNYMoaSixV5FCfCGFYUjkUKvID2re6kWnhGdoHw4oMdbHyh1wb8fQnIHs+y7Ij9nsVX1t9h2WZMF6QK0ZgQiY69NopgdWzNTbqFZ3gCEbzAY/PK/tP3NRhT4LLkHSd/rP6heKmjoxd2xUrbUF0THYdyQ2A7WnMFZn0P0euqiCX615+3PR8E/tPsB7InASk5/sK612tnlqiisvORAZShObnFFV/XECkEaMZ0a51b83jFMXF70GG3rxmUrg3pv2M/kT3msmYcn1wx67Ry4+dVhjsyYDkGv9/F9wLKakqJlQaIGW0HMLSwXFbp6coxlsVNPHYokbjNS3/s+AKQOqgAKauJ3rXwo41zvVww1O6/iykGhraNXQCU10WIDhF6MiIYvd0umbRXGBC6Z/MPo4ZV97b76a78zexHsgdclnXhSf9Q/7GocUgkYiPOtDWFsXsz5lZTVhVFR2znDHcJuztyZNL+pDadxmMdLh4bX0qdRMjEc7BYSNnx51c9UFtbqm+/0iKBr0ybU0+gO5KDIkLG8zj6pEaSFZFR8+3i0M98Xhl74svkArkxos/c0fa0l9292Vb7nYXUzy79yzHnNei6V7ZI4OtQoJRdgjJUVERIVjijFtdFV9XVtudjxvaLY+sbA9K1afA97IcyaUCiCfvTJ19WvzA7kJeq2iSoEiuNDhVwxWCuColSm5JSa9RSdFvcyJH3gikBQ1Esx/DifR3XAoP7IyCTfeqGd17W2Np4dCmgRKIO6f4cTswaYlCLk3giEUNNfZjejpSyFscaDw549PV6TAEWRcD1hV+3p7esTpWyn8qkLKRpXvkjzccmVQqd5PmcixPdBkbRNVg2VNdHwpEXo87yFLJZf8rACBEx9GzOyJbVqVnsxzIZQP5+wcU1x3rh2zDDmLEdCNvTJbX1sR1AGklcV+npzDNV3TaqihVXnv6PLV8C2g4qQI5YWP5zJ25UCIZd8yKgAVTVhnXGWOSi7yudbdkpqTWKYERLbF32rxufDbzgJvZzmWjae/mc91TFCEYaSB9mVPESOzwDOEaAJQjJwt0LZ6N/i+2IPn7bprbBntwiDgCZkIU0LSj753jcGeUkmWAMVFbbY3BToXdqb80x0X6qcWcr4SaWrri/QzreGpzGASITAWTW9HmJOb6vIzfnqJJI2ju01ez6mbBjpKMtX9hOnRrL8BHWLu+Rjc/1Nu1v1fgeAcRgfap5YRJGPIWkGGNIlkVGjM3F5raudpfAD6YEDC0k0Vtf7ee1hztPBFo5gGTcgDSdkLjcy428olWhJGF2oU12BMPQ2+WSz/vjA0O351MYmoE12sdFhdTmDC/8tv180Bc5wGS8gNjljdFm9Rn1/RmJpD1iE4ERQ38qTyYzgW6RAgiZgRzdG1PhzeqI5oeoMpjK8sTtLVdD8BAHoIwXkONqZsSHjoeNVNxZ9q4nZ1UVwZBK5Rnon2DrjoLvevS09JFN59iytn0n09n+o4Ln+Tz6/U1fAb2DA1TGC8j8ZGNk1D1yRXFzwTYgKLylJoCu9hyD/RPvo1KUtvXdEE7RIBJzdqHji6AbS/jjjRu+CXyLA1jGWYfInJIKS7OpYOSEV4TO9jylSRvLFoJAyWUDshkfYybX8iliaJpRRWdrP7GSGE2zqujrT2/3qtQwkVCjPPSNdbdA8FUOcBkXIJG4meblkbH3J5T+vm0HLqXwLqciYBOqI0RQDSBqMX1eHZ7r7QBG8VaCSMCyr2/893zOu46DQMYFiFViB/jj2S6SHV/JvJtpbVH5uWx+h1mLRebWti35803r786m89dwkMi4YkiuxxXjhCnlBNS5J+vunQZfgm0beezfNj042J27jINIxmUhQaC9WjwzsO+PtqvjWPLoLRsfTLVm3sdBJuPMsvSv/Vvz+xaJcDCABgZZ9t237jkYwZhI2vvQ1rUDe+9s8LB0iCpGZNmNG+4c6PYu5SCV8QLSt+WVwWfsqK26F2HRYsmnotkBV/7wz+u/mcvlP85BLON+XUW6x32ptN6+pqw6tm3K916ARBDtXJ+Wx2/ddLkS3MxBLhN5f0hr28u57qYF8fdGS+wpa9MpWgUKVsRizZPd2VX3th0HPMYhINbElBU8t/H5dHf5dOe9ZfVR1aBQLBbT4cmOoyp0nRRP4loRQ/ubaVbds+UPG1f2Hwt0cYjIZJf4Uc0nVDw059zyo0sroup7gYgUV7eM+8IhAOFEBUWxY8L6F1JseDb1l65N2f8JPMshJrvrc85sXlj29YbZiTOaT0jiu6BBce+iUKnvXLlocZ/QgISvmxvozPH2c31seG7wR24u/x1gI4eo7KkgkDQi1804qeya8mnRGVUzSqiYHsGoEHhhrAkIdwutuDDQ7tGzKU13Sz7dsTb9y97Nmd8Aj3BYpqzsPgNYVFobiZUdYYv6GvFz1LuDSM/67GbQ1cDfgNWHIdhR/j8kbNLaZRHs3AAAAABJRU5ErkJggg==">

