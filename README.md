[![Build Status](https://travis-ci.org/gizaju10/django.svg?branch=master)](https://travis-ci.org/gizaju10/django)

# ZERO TOKYO ０円で楽しむ東京観光

## URL
https://gizagiza.work/

### PC画面例
![PC](https://giza-s3.s3-ap-northeast-1.amazonaws.com/pc2.gif)

<div align="center">
  <h3>スマホ画面例</h3>
</div>
<div align="center">
  <img src="" width=25% title＝"スマホ">
 </div>
<br>
<h2>概要</h2>
<h3>東京23区内の「0円で東京観光」できる場所を調べられるアプリです。</h3>
<strong><p>《操作が分かりやすい》</p></strong>
<ol style="list-style-type: decimal">
  <li>『最新スポット』</li>
  <li>『23区エリア』</li>
  <li>『天気』</li>
  <li>『検索』</li>
</ol>
上記、4点から<strong>簡単に23区内の観光スポットを探す</strong>ことができます。
<br>

<h2>使用例</h2>
<h3>東京観光中のAさん</h3>
<h4>16:00（東京駅構内）</h4>
<pre>
  Aさん:晩御飯に千代田区のお店を18時に予約したけど、あと2時間時間潰せないかな？
  (23区エリアから千代田区を選択)
  Aさん:『インターメディアテク』って場所面白そう。18:00までやってるみたいだし、行ってみよう!
</pre>

<h4>18:30(予約していた飲食店内)</h4>
<pre>
(<a href="https://gizagiza.work/blog/post/21/" target="_blank">『インターメディアテク』</a>のページを開く)
Aさん：コメント欄あるんだ！『インターメディアテク』楽しかったし、コメントでも残そうかな。
(コメント投稿用に会員登録)
Aさん：無料とは思えない程、沢山の展示を見れて楽しかったです。
(コメントを投稿)
Bさん：私も行ったことあります。ミンククジラの骨格標本に感動しました！
(返信を投稿)
Cさん：今度、東京に行く用事があります。私も沢山の展示を見たいので行ってみます!!
(返信を投稿)
</pre>
この様に<strong>東京観光での隙間時間に、お金を掛けずに遊べるスポットを探す</strong>ことができます。
<br>

<h2>実装した機能</h2>
<ul>
<li>レスポンシブ対応</li>
<li>ユーザー登録・ログイン機能(メール認証有)</li>
<li>ログイン保持機能</li>
<li>投稿機能</li>
<li>投稿一覧・投稿詳細表示機能</li>
<li>投稿管理機能</li>
<li>投稿編集機能(下書き保存可)</li>
<li>カテゴリ、タグ機能</li>
<li>カテゴリ、タグ一覧機能</li>
<li>カテゴリ、タグ管理機能</li>
<li>画像ファイルのアップロード機能</li>
<li>ページネーション機能</li>
<li>いいね機能</li>
<li>検索機能</li>
<li>コメント、コメントの返信投稿機能</li>
<li>コメント、コメントの返信承認、削除機能</li>
<li>お問い合わせ機能</li>
<li>Travis CI 自動ビルド・自動テスト</li>
</ul>
  
<h2>使用技術</h2>
<ul>
  <li>Python: 3.7.6</li>
  <li>Django: 3.0.7</li>
  <li>PostgreSQL: 9.6.8</li>
  <li>HTML/CSS/Bootstrap</li>
  <li>JavaScript/jQuery</li>
  <li>Docker/docker-compose</li>
  <li>AWS</li>
  <li>Travis CI</li>
  <li>Git/GitHub</li>
  <li>Nginx</li>
  <li>Gunicorn</li>
  <li>Google Maps API</li>
</ul>

<h2>インフラ</h2>
<ul>
  <li>インフラ構成図</li>
</ul>

![zerotokyo.png](https://giza-s3.s3-ap-northeast-1.amazonaws.com/zerotokyo.png)
