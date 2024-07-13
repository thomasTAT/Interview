# Pygame 

此遊戲的玩法是，一個哥布林會在一定範圍內來回走動，玩家需要避開哥布林的追擊。如果被哥布林碰到，遊戲即告失敗。玩家在避開哥布林的同時，需要射擊哥布林。每次射擊會讓哥布林扣血，當哥布林的血量減少到零時，哥布林會消失。

這個 Pygame 遊戲主要利用了 Python 面向對象編程（OOP）來實現。遊戲中有三個類，分別是 Man、Goblin 和 Bullet。每個對象都有自己的屬性，如座標和碰撞檢測框。

在主循環中，進行了 Man 和 Goblin 的碰撞檢測，以及 Goblin 和 Bullet 的碰撞檢測。

Man 的移動通過 Pygame 檢測鍵盤是否有上下移動或跳躍的指令，如果有，則在主循環中修改 Man 的 x 和 y 座標。

Goblin 的移動則設置了起點和終點，在主循環中修改 Goblin 的 x 座標，使其在這兩點之間來回移動。

<div style="display: flex; gap: 20px;">
    <img src="Show%20case/game%20play%201.png" height="250">
    <img src="Show%20case/game%20play%202.png" height="250">
    <img src="Show%20case/game%20play%203.png" height="250">
</div>