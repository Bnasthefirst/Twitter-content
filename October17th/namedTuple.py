from collections import namedtuple
Point = namedtuple( 'Point', ['x',
'y' ])
p = Point( 10,20 )


p = p._replace(x=100)



p._asdict() # {'x': 100, 'y': 20}
