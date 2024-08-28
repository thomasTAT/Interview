# Abstract
使用了 bootstrap，grid，media query，去完成這個前端靜態網頁，實現響應式。

<img src="show case/website.png" height=300px>

## index 頁面

**Header**: 使用了 bootstrap fix top ，讓他永遠置頂。hearer 使用了 bootstrap 的 `.container` 和 `.row`，實現 responsive css。`.row` 是一個 flex box，可以用 `align-items` 和 `justify` 對 `.row` 裡面的 box 進行排版。

<img src="show case/header.png" height= 150px>


**導航欄**: 利用 media query 做了個 Hamburger Menu，當窗口縮小，make appointment 會消失。窗口再繼續消失，nav 就會被隱藏，需要點擊三行才可以展開。 實現方法是利用了 `position`，把 nav 移動到下方，在用 polygon 將其隱藏。點擊 polygon 設置將 nav 顯示。

<div style="display: flex; gap: 100px;">
  <img src="show case/hamburger 1.png" height="150px">
  <img src="show case/hamburger 2.png" height="150px">
</div>


css 上用了 `scroll-behavior: smooth`,點擊鏈接跳轉,更加 smooth.

**section `.home`** 部分用了，圖片作為 background。利用 bootstrap 製造 .container .row。裡面裝著 .content， .content 裝著 標題 form等訊息。 限制了 .content 的寬, 因此內容靠左。

<div> <img src="show case/home.png" height="200px"> </div>


**recommend section** 抄了 bootstrap 的代碼,實現了幻燈片(Carrousel).
<div><img src="show case/recommendation.png" height="200px"></div>



**about us section** 利用了 col-md-6 , 在 row 的基礎上,劃分 2 個column. 左邊顯示圖片,右邊顯示諮詢.
<div><img src="show case/about.png" height="200px"></div>


**doctor section** 利用了 `grid-template-columns: repeat(auto-fit,minmax(30rem,1fr)` 自動生成 column. container 縮小, 醫生box 會根據視窗大小 warp.

<div><img src="show case/doctor.png" height="400px"></div>


下面的section 做法完全一致.

## Doctor 子頁面
**Header**
 和 home page 類似.

**about**
利用了 Bootstrap col-md-6 進行佈局.

## 健康文章子子頁面
利用了 Bootstrap col-md-6 進行佈局.
