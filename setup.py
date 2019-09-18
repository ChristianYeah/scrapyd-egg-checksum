import setuptools

setuptools.setup(
    name='scrapyd_egg_checksum',
    version='0.1',
    author="Xiaodong Ye",
    author_email="470504024@qq.com",
    url='https://github.com/ChristianYeah/scrapyd-egg-checksum',
    description="Get the checksum of eggs in case of building distributed scrapy clusters",
    packages=["scrapyd_egg_checksum"],
    install_requires=[
        'scrapy',
        'scrapyd',
    ],
    license='MIT'
)
