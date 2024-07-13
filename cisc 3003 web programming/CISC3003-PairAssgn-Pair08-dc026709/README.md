# Abstract
這個網站可以通過拆分成多個「行容器」（row container），每個行容器使用 Flexbox 來設計。

## cisc3003-PairAssgn.html

**Humber** Humber 菜單利用了 `overflow: hidden`、媒體查詢（media query）、定位（position）和 JavaScript 來實現。在視窗寬度小於某個特定值時，利用 `position` 將導航欄移動到標題（header）下方，並在標題處顯示一個菜單按鈕。這時將導航欄的父容器高度設置為 0，利用 `overflow: hidden` 隱藏內容。當點擊菜單按鈕時，利用 JavaScript 將導航欄父容器的高度設置為正常值，這樣內容就會顯示出來，導航菜單可以正常使用。

<img src="show%20case/humber.png" alt="圖片描述" height =300 >


**row** 網站的每一行都是一個大的容器，使用 Flexbox 並設置了 `flex-wrap` 屬性。在每個行容器內部，包含了兩個子容器（box），利用 `flex-basis: 50%` 分別佔據了該行一半的空間，從而實現了響應式設計。
<p></p>


<div style="display: flex; gap: 100px;">
    <img src="show%20case/row.png" alt="圖片描述" height =300 style="margin-right: 100px;" >
    <img src="show%20case/warp.png" alt="圖片描述" height =300 >
</div>

<p></p>

**side bar 和 content** 有一個 flexbox 容器，裡面包含了側邊欄（side bar）區塊和內容（content）區塊。側邊欄佔用橫向空間的 15%，內容區塊佔用橫向空間的 85%。內容區塊進一步被分割成多個橫排（row）。

<div>
<img src="show%20case/content.png" alt="圖片描述" height =300 >
</div>

其餘部分做法類似.