# python4sem5pr2part
##Testing default start state:

```
START_STATE:
Write Index Command:
0 - Use DEFAULT_START_STATE:
DEFAULT_START_STATE = (
 player = 'alice'
 alice_room = 'west room'
 bob_room = 'east room'
 red_key = 'east room'
 blue_key = 'west room'
 green_key = 'east room'
);
1 - Create custome START_STATE;
2 - Create START_STATE with random values.
Write Command:
0
START_STATE = (
 player = 'alice'
 alice_room = 'west room'
 bob_room = 'east room'
 red_key = 'east room'
 blue_key = 'west room'
 green_key = 'east room'
);
List with min steps:
-Min finish State-Node with 10 steps
  player = 'alice'
  alice_room = 'red room'
  bob_room = 'blue room'
  red_key = 'alice'
  blue_key = 'bob'
  green_key = 'bob'
digraph {
n0 [style="filled",fillcolor="dodgerblue",shape="circle"]
n1 [shape="circle"]
n2 [shape="circle"]
n3 [shape="circle"]
n4 [shape="circle"]
n5 [shape="circle"]
n6 [shape="circle"]
n7 [shape="circle"]
n8 [shape="circle"]
n9 [shape="circle"]
n10 [shape="circle"]
n11 [shape="circle"]
n12 [shape="circle"]
n13 [shape="circle"]
n14 [shape="circle"]
n15 [shape="circle"]
n16 [shape="circle"]
n17 [style="filled",fillcolor="green",shape="circle"]
n18 [style="filled",fillcolor="darkgreen",shape="circle"]
n19 [shape="circle"]
n20 [shape="circle"]
n21 [shape="circle"]
n22 [shape="circle"]
n23 [shape="circle"]
n24 [shape="circle"]
n25 [shape="circle"]
n26 [shape="circle"]
n27 [shape="circle"]
n28 [shape="circle"]
n29 [shape="circle"]
n30 [shape="circle"]
n31 [shape="circle"]
n32 [shape="circle"]
n33 [shape="circle"]
n34 [shape="circle"]
n35 [shape="circle"]
n36 [shape="circle"]
n37 [shape="circle"]
n38 [shape="circle"]
n39 [shape="circle"]
n40 [shape="circle"]
n41 [shape="circle"]
n42 [shape="circle"]
n43 [shape="circle"]
n44 [shape="circle"]
n45 [shape="circle"]
n46 [shape="circle"]
n47 [shape="circle"]
n48 [shape="circle"]
n49 [shape="circle"]
n50 [shape="circle"]
n51 [shape="circle"]
n52 [shape="circle"]
n53 [shape="circle"]
n54 [shape="circle"]
n55 [shape="circle"]
n56 [shape="circle"]
n57 [shape="circle"]
n58 [shape="circle"]
n59 [shape="circle"]
n60 [shape="circle"]
n61 [shape="circle"]
n62 [shape="circle"]
n63 [shape="circle"]
n64 [shape="circle"]
n65 [shape="circle"]
n66 [shape="circle"]
n67 [shape="circle"]
n68 [shape="circle"]
n69 [shape="circle"]
n70 [shape="circle"]
n71 [shape="circle"]
n72 [shape="circle"]
n73 [shape="circle"]
n74 [shape="circle"]
n75 [shape="circle"]
n76 [shape="circle"]
n77 [shape="circle"]
n78 [shape="circle"]
n79 [shape="circle"]
n80 [shape="circle"]
n81 [shape="circle"]
n82 [shape="circle"]
n83 [shape="circle"]
n84 [shape="circle"]
n85 [shape="circle"]
n86 [shape="circle"]
n87 [shape="circle"]
n88 [shape="circle"]
n89 [shape="circle"]
n90 [shape="circle"]
n91 [shape="circle"]
n0 -> n1
n0 -> n90
n1 -> n0
n1 -> n2
n1 -> n66
n2 -> n3
n2 -> n46
n3 -> n2
n3 -> n4
n4 -> n5
n5 -> n4
n5 -> n6
n6 -> n7
n6 -> n45
n7 -> n6
n7 -> n8
n7 -> n25
n7 -> n36
n8 -> n7
n8 -> n9
n9 -> n10
n10 -> n11
n10 -> n9
n10 -> n13
n10 -> n7
n10 -> n40
n11 -> n10
n11 -> n12
n12 -> n11
n13 -> n14
n13 -> n24
n13 -> n25
n13 -> n41
n14 -> n15
n14 -> n13
n14 -> n19
n15 -> n16
n16 -> n17
n16 -> n15
n17 -> n18
n18 -> n17
n19 -> n20
n19 -> n14
n20 -> n21
n21 -> n18
n21 -> n22
n21 -> n20
n22 -> n21
n22 -> n23
n23 -> n22
n24 -> n23
n24 -> n13
n24 -> n9
n25 -> n26
n25 -> n28
n25 -> n29
n26 -> n25
n26 -> n27
n27 -> n26
n28 -> n25
n28 -> n8
n28 -> n24
n29 -> n30
n30 -> n31
n30 -> n29
n30 -> n33
n30 -> n42
n30 -> n28
n31 -> n30
n31 -> n32
n32 -> n31
n33 -> n34
n33 -> n36
n33 -> n37
n33 -> n8
n34 -> n33
n34 -> n35
n35 -> n34
n36 -> n33
n36 -> n29
n37 -> n38
n37 -> n40
n37 -> n9
n38 -> n37
n38 -> n39
n39 -> n38
n40 -> n37
n40 -> n41
n40 -> n36
n41 -> n42
n41 -> n29
n42 -> n43
n42 -> n41
n42 -> n37
n42 -> n24
n43 -> n42
n43 -> n44
n44 -> n43
n45 -> n6
n46 -> n47
n46 -> n65
n47 -> n46
n47 -> n48
n47 -> n49
n47 -> n64
n47 -> n10
n48 -> n47
n48 -> n8
n49 -> n50
n49 -> n56
n49 -> n57
n49 -> n13
n50 -> n49
n50 -> n51
n51 -> n52
n51 -> n50
n51 -> n27
n52 -> n53
n53 -> n54
n53 -> n52
n54 -> n53
n54 -> n55
n54 -> n22
n55 -> n54
n56 -> n55
n56 -> n49
n56 -> n48
n56 -> n28
n57 -> n58
n57 -> n41
n58 -> n59
n58 -> n57
n58 -> n61
n58 -> n56
n58 -> n30
n59 -> n58
n59 -> n60
n60 -> n59
n60 -> n44
n61 -> n62
n61 -> n64
n61 -> n48
n61 -> n33
n62 -> n61
n62 -> n63
n63 -> n62
n63 -> n39
n64 -> n61
n64 -> n57
n64 -> n40
n65 -> n46
n65 -> n45
n66 -> n67
n66 -> n89
n66 -> n46
n67 -> n66
n67 -> n68
n67 -> n85
n67 -> n82
n68 -> n67
n68 -> n69
n69 -> n70
n69 -> n81
n70 -> n71
n70 -> n69
n70 -> n73
n71 -> n70
n71 -> n72
n71 -> n6
n72 -> n71
n73 -> n74
n74 -> n75
n74 -> n73
n74 -> n77
n74 -> n69
n75 -> n74
n75 -> n76
n75 -> n31
n76 -> n75
n77 -> n78
n77 -> n80
n77 -> n81
n78 -> n77
n78 -> n79
n78 -> n43
n79 -> n78
n80 -> n77
n80 -> n73
n81 -> n82
n82 -> n83
n82 -> n81
n82 -> n70
n82 -> n80
n83 -> n82
n83 -> n84
n83 -> n11
n84 -> n83
n85 -> n86
n85 -> n80
n86 -> n87
n86 -> n85
n86 -> n68
n86 -> n74
n87 -> n86
n87 -> n88
n87 -> n59
n88 -> n87
n88 -> n79
n89 -> n66
n89 -> n72
n90 -> n91
n91 -> n90
n91 -> n5
n91 -> n71
}
```

###Picture:


##Testing random start state:

```
START_STATE:
Write Index Command:
0 - Use DEFAULT_START_STATE:
DEFAULT_START_STATE = (
 player = 'alice'
 alice_room = 'west room'
 bob_room = 'east room'
 red_key = 'east room'
 blue_key = 'west room'
 green_key = 'east room'
);
1 - Create custome START_STATE;
2 - Create START_STATE with random values.
Write Command:
2
START_STATE = (
 player = 'alice'
 alice_room = 'west room'
 bob_room = 'east room'
 red_key = 'west room'
 blue_key = 'east room'
 green_key = 'east room'
);
List with min steps:
-Min finish State-Node with 5 steps
  player = 'bob'
  alice_room = 'red room'
  bob_room = 'blue room'
  red_key = 'alice'
  blue_key = 'bob'
  green_key = 'east room'
digraph {
n0 [style="filled",fillcolor="dodgerblue",shape="circle"]
n1 [shape="circle"]
n2 [shape="circle"]
n3 [shape="circle"]
n4 [shape="circle"]
n5 [shape="circle"]
n6 [style="filled",fillcolor="darkgreen",shape="circle"]
n7 [style="filled",fillcolor="green",shape="circle"]
n8 [shape="circle"]
n9 [shape="circle"]
n10 [shape="circle"]
n11 [shape="circle"]
n12 [shape="circle"]
n13 [shape="circle"]
n14 [style="filled",fillcolor="darkgreen",shape="circle"]
n15 [style="filled",fillcolor="darkgreen",shape="circle"]
n16 [shape="circle"]
n17 [shape="circle"]
n18 [shape="circle"]
n19 [shape="circle"]
n20 [shape="circle"]
n21 [shape="circle"]
n22 [shape="circle"]
n23 [shape="circle"]
n24 [shape="circle"]
n25 [shape="circle"]
n26 [shape="circle"]
n27 [shape="circle"]
n28 [shape="circle"]
n29 [shape="circle"]
n30 [shape="circle"]
n31 [shape="circle"]
n32 [shape="circle"]
n33 [shape="circle"]
n34 [shape="circle"]
n35 [shape="circle"]
n36 [shape="circle"]
n37 [shape="circle"]
n38 [shape="circle"]
n39 [shape="circle"]
n40 [shape="circle"]
n41 [shape="circle"]
n42 [shape="circle"]
n43 [shape="circle"]
n44 [shape="circle"]
n45 [shape="circle"]
n46 [shape="circle"]
n47 [shape="circle"]
n48 [shape="circle"]
n49 [shape="circle"]
n50 [shape="circle"]
n51 [shape="circle"]
n52 [shape="circle"]
n53 [shape="circle"]
n54 [shape="circle"]
n55 [shape="circle"]
n56 [shape="circle"]
n57 [shape="circle"]
n58 [shape="circle"]
n59 [shape="circle"]
n60 [shape="circle"]
n61 [shape="circle"]
n62 [shape="circle"]
n63 [shape="circle"]
n64 [shape="circle"]
n65 [shape="circle"]
n66 [shape="circle"]
n67 [shape="circle"]
n68 [shape="circle"]
n69 [shape="circle"]
n70 [shape="circle"]
n71 [shape="circle"]
n72 [shape="circle"]
n73 [shape="circle"]
n74 [shape="circle"]
n75 [shape="circle"]
n76 [shape="circle"]
n77 [shape="circle"]
n78 [shape="circle"]
n79 [shape="circle"]
n80 [shape="circle"]
n81 [shape="circle"]
n82 [shape="circle"]
n83 [shape="circle"]
n84 [shape="circle"]
n85 [shape="circle"]
n86 [shape="circle"]
n87 [shape="circle"]
n88 [shape="circle"]
n89 [shape="circle"]
n90 [shape="circle"]
n91 [shape="circle"]
n92 [shape="circle"]
n93 [shape="circle"]
n94 [shape="circle"]
n95 [shape="circle"]
n96 [shape="circle"]
n97 [shape="circle"]
n98 [shape="circle"]
n99 [shape="circle"]
n100 [shape="circle"]
n101 [shape="circle"]
n102 [shape="circle"]
n103 [shape="circle"]
n0 -> n1
n0 -> n100
n1 -> n0
n1 -> n2
n1 -> n72
n2 -> n3
n2 -> n9
n2 -> n54
n3 -> n4
n4 -> n3
n4 -> n5
n5 -> n6
n5 -> n8
n6 -> n7
n7 -> n6
n8 -> n5
n9 -> n2
n9 -> n10
n10 -> n11
n10 -> n19
n11 -> n12
n12 -> n7
n12 -> n11
n12 -> n13
n13 -> n14
n13 -> n16
n13 -> n18
n14 -> n15
n15 -> n14
n16 -> n13
n16 -> n17
n17 -> n16
n18 -> n13
n19 -> n8
n19 -> n10
n19 -> n20
n20 -> n21
n20 -> n23
n20 -> n53
n21 -> n22
n22 -> n15
n22 -> n21
n23 -> n20
n23 -> n24
n23 -> n33
n23 -> n49
n24 -> n17
n24 -> n23
n24 -> n25
n25 -> n26
n26 -> n27
n26 -> n25
n26 -> n23
n26 -> n29
n26 -> n48
n27 -> n26
n27 -> n28
n28 -> n27
n29 -> n30
n29 -> n32
n29 -> n33
n29 -> n44
n30 -> n29
n30 -> n31
n31 -> n30
n32 -> n29
n32 -> n25
n33 -> n34
n33 -> n36
n33 -> n37
n34 -> n33
n34 -> n35
n35 -> n34
n36 -> n33
n36 -> n32
n36 -> n24
n37 -> n38
n38 -> n39
n38 -> n37
n38 -> n41
n38 -> n50
n38 -> n36
n39 -> n38
n39 -> n40
n40 -> n39
n41 -> n42
n41 -> n44
n41 -> n45
n41 -> n32
n42 -> n41
n42 -> n43
n43 -> n42
n44 -> n41
n44 -> n37
n45 -> n46
n45 -> n48
n45 -> n25
n46 -> n45
n46 -> n47
n47 -> n46
n48 -> n45
n48 -> n49
n48 -> n44
n49 -> n50
n49 -> n37
n50 -> n51
n50 -> n49
n50 -> n45
n50 -> n24
n51 -> n50
n51 -> n52
n52 -> n51
n53 -> n18
n53 -> n20
n54 -> n55
n54 -> n57
n54 -> n71
n55 -> n56
n56 -> n55
n56 -> n22
n57 -> n54
n57 -> n58
n57 -> n59
n57 -> n70
n57 -> n26
n58 -> n57
n58 -> n24
n59 -> n60
n59 -> n62
n59 -> n63
n59 -> n29
n60 -> n59
n60 -> n61
n61 -> n60
n61 -> n35
n62 -> n59
n62 -> n58
n62 -> n36
n63 -> n64
n63 -> n44
n64 -> n65
n64 -> n63
n64 -> n67
n64 -> n62
n64 -> n38
n65 -> n64
n65 -> n66
n66 -> n65
n66 -> n43
n67 -> n68
n67 -> n70
n67 -> n58
n67 -> n50
n68 -> n67
n68 -> n69
n69 -> n68
n69 -> n47
n70 -> n67
n70 -> n63
n70 -> n48
n71 -> n54
n71 -> n53
n72 -> n73
n72 -> n99
n72 -> n54
n73 -> n72
n73 -> n74
n73 -> n95
n73 -> n92
n74 -> n73
n74 -> n75
n75 -> n76
n75 -> n80
n75 -> n91
n76 -> n77
n77 -> n78
n77 -> n76
n78 -> n77
n78 -> n79
n78 -> n13
n79 -> n78
n80 -> n81
n80 -> n75
n80 -> n83
n81 -> n80
n81 -> n82
n81 -> n20
n82 -> n79
n82 -> n81
n83 -> n84
n84 -> n85
n84 -> n83
n84 -> n87
n84 -> n75
n85 -> n84
n85 -> n86
n85 -> n39
n86 -> n85
n87 -> n88
n87 -> n90
n87 -> n91
n88 -> n87
n88 -> n89
n88 -> n42
n89 -> n88
n90 -> n87
n90 -> n83
n91 -> n92
n92 -> n93
n92 -> n91
n92 -> n80
n92 -> n90
n93 -> n92
n93 -> n94
n93 -> n27
n94 -> n93
n95 -> n96
n95 -> n90
n96 -> n97
n96 -> n95
n96 -> n74
n96 -> n84
n97 -> n96
n97 -> n98
n97 -> n65
n98 -> n97
n98 -> n89
n99 -> n72
n99 -> n82
n100 -> n101
n100 -> n103
n101 -> n102
n102 -> n101
n102 -> n12
n102 -> n78
n103 -> n100
n103 -> n19
n103 -> n81
}
```

###Picture
