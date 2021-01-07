var operator_string = '+-/*';
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+-'];

for (var i = 0; i < operator_string.length; i++) {
    document.getElementById(operator_string[i]).disabled = true;
}

function clear() {
    console.log(document.getElementById("expression").innerText);
    setExpression("");

}

function setExpression(input) {
    if (input == '+-') {
        // add minus sign in front expression string
        if (parseFloat(document.getElementById("expression").innerText) > 0) {
            document.getElementById("expression").innerText = '-' + document.getElementById("expression").innerText
        }
        // will subtract first character of expression string to make it positive
        else if (parseFloat(document.getElementById("expression").innerText) < 0) {
            document.getElementById("expression").innerText = document.getElementById("expression").innerText.substr(1);
        }

    } else if (input == 'backspace') {
        // delete last character in string
        document.getElementById("expression").innerText = document.getElementById("expression").innerText.slice(0, -1);

    } else {
        if (input == "") {
            document.getElementById("expression").innerText = input;
        } else {
            document.getElementById("expression").innerText += input;
        }
    }

    if (input == document.getElementById(".").id) {
        document.getElementById(".").disabled = true;
    }

    // disables all operators after input==operator is clicked

    if (operator_string.includes(input)) {
        for (var i = 0; i < operator_string.length; i++) {
            document.getElementById(operator_string[i]).disabled = true;
        }
        // enables decimal after operator is clicked
        document.getElementById(".").disabled = false;
    }

    // enables operators buttons after a number is clicked
    if (nums.includes(input)) {
        for (var i = 0; i < operator_string.length; i++) {
            document.getElementById(operator_string[i]).disabled = false;
        }
    }

}

function solve(input = "") {
    var number = document.getElementById("expression").innerText;

    // for sqrt eval
    if (input == "Sqrt") {
        solution = Math.sqrt(number);
        clear();
        setExpression(solution);
    }
    // for regular eval
    else {
        solution = eval(number);
        clear();
        setExpression(solution);
    }

    //enable operators after evaluation
    for (var i = 0; i < operator_string.length; i++) {
        document.getElementById(operator_string[i]).disabled = false;
    }
}