// var questions = document.querySelectorAll("#questions .question")
var questions = document.querySelectorAll("#questions .question form")
console.log(questions.length)
var Test = []
for(let i = 0; i < questions.length; i++){
    // Test.append(questions[i])
    var ques = {
        "q": questions[i].querySelector("p").textContent.trim(),
        "a": [],
    }
    // var title = questions[i].querySelector("p").textContent.trim(),
    // answers = []
    questions[i].querySelectorAll("fieldset ul li").forEach(a => ques['a'].push(a.innerText.trim()))
    Test.push(ques)
}
console.log(Test)