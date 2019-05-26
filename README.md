# 概要
Twitter API から、にじさんじライバーのフォロワーを取得して分析する。  
詳しくは[ブログ記事](https://p-n-d.hatenablog.com/entry/2019/05/26/041616)参照。

![t-SNE によるにじさんじライバーの埋め込み](https://cdn-ak.f.st-hatena.com/images/fotolife/P/P_N_D/20190526/20190526001415.png)


# 使い方
1. [Twitter Developers](https://developer.twitter.com) で app を作成
2. このレポジトリを clone 

```
git clone https://github.com/swen128/twitter_follower_analysis.git
cd twitter_follower_analysis
```

3. `.env` ファイルを作成し、Twitter app の API key を入力

```
cp .env.sample .env
vi .env
```

4. `fetch_nijisanji_livers.py` を実行して、全にじさんじライバーのアカウント情報を取得
5. `fetch_followers.py` を実行して、全フォロワー ID を取得
6. `fetch_icons.py` を実行して、全ライバーのアイコン画像を取得
7. `EDA.ipynb` でフォロワーを分析 