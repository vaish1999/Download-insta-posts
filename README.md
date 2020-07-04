# Download-insta-posts
This package will help you download your favourite celebrity post and also any of your friends' profile picture.

Installation:

```python
pip install pyinsta
```

1. Download your favourite celebrity's n<sup>th</sup> picture of m<sup>th</sup> post as follows:

```python
from pyinsta.download import post
post("username of the celebrity",m,n)
```

Output: 
The picture or video gets saved in the folder called instagram_downloads, which will be loacted in the command running directory.
Nomenclature of the picture or video saved will be:
"username_m_n.jpg/.mp4"

2. Download your favourite celebrity's n<sup>th</sup> post which has only a single picture in it, as follows:

```python
from pyinsta.download import post
post("username of the celebrity",n)
```

Output: 
The picture or video gets saved in the folder called instagram_downloads, which will be loacted in the command running directory.
Nomenclature of the picture or video saved will be:
"username_n.jpg/.mp4"

3. Download any of your friends' profile picture as follows:

```python
from pyinsta.download import profile_pic
profile_pic("username of the celebrity")
```

Output: 
The profile picture gets saved in the folder called instagram_downloads, which will be loacted in the command running directory.
Nomenclature of the picture saved will be:
"username_profile_pic.jpg"



