<html>
<head>
    <title>Addition</title>
    <script>
        function display(id_name,result_name){
       document.getElementById(result_name).innerHTML = document.getElementById(id_name).value;
       }
       function calculate(id1,id2,result_id) {
       document.getElementById(result_id).innerHTML = parseInt(document.getElementById(id1).value)+parseInt(document.getElementById(id2).value)
       }
    </script>
</head>
<body>
<div class="input">
    Enter 1st Number:
    <input type="text" id="input1_text">
    <button type="button" onclick="display('input1_text','input1')">Enter 1st Number</button>
    <span id="input1"></span>
</div>

<div class="input">
    Enter 2nd Number:
    <input type="text" id="input2_text">
    <button type="button" onclick="display('input2_text','input2')">Enter 2nd Number</button>
    <span id="input2"></span>
</div>
<div class="result">
    <button type="button" onclick="calculate('input1_text','input2_text','result_value')">Calculate</button>
    <span id="result_value"></span>
</div>
</body>
</html>