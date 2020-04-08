// var el = x => document.getElementById(x);

// function showPicker() {
//   el("file-input").click();
// }

// function showPicked(input) {
//   el("upload-label").innerHTML = input.files[0].name;
//   var reader = new FileReader();
//   reader.onload = function(e) {
//     el("image-picked").src = e.target.result;
//     el("image-picked").className = "";
//   };
//   reader.readAsDataURL(input.files[0]);
// }

// function analyze() {
//   var uploadFiles = el("file-input").files;
//   if (uploadFiles.length !== 1) alert("Please select a file to analyze!");

//   el("analyze-button").innerHTML = "Analyzing...";
//   var xhr = new XMLHttpRequest();
//   var loc = window.location;
//   xhr.open("POST", `${loc.protocol}//${loc.hostname}:${loc.port}/analyze`,
//     true);
//   xhr.onerror = function() {
//     alert(xhr.responseText);
//   };
//   xhr.onload = function(e) {
//     if (this.readyState === 4) {
//       var response = JSON.parse(e.target.responseText);
//       el("result-label").innerHTML = `Result = ${response["result"]}`;
//     }
//     el("analyze-button").innerHTML = "Analyze";
//   };

//   var fileData = new FormData("#formReview");
//   fileData.append("file", uploadFiles[0]);
//   xhr.send(fileData);
// }


$(function() {
  // Get the form.
  $("#formreview").on('submit', function(e){
  e.preventDefault()
  var form = new FormData('#formreview');
  console.log(form)

  e.preventDefault();
  var trestbps = $.trim($("#trestbps").val()); 
  var chol = $.trim($("#chol").val());
  var thalach = $.trim($("#thalach").val());
  var oldpeal = $.trim($("#oldpeal").val());
  var sex = $.trim($("#sex").val());
  var chestpain = $.trim($("#chestpain").val());
  var fbs = $.trim($("#fbs").val());
  var R_ECG = $.trim($("#R_ECG").val());
  var angina = $.trim($("#angina").val());
  var slope = $.trim($("#slope").val());
  var ca = $.trim($("#ca").val());
  var age = $.trim($("#age").val());

  if (trestbps==''){
    alert('trestbps address is required');
    return;
  }
  else if (chol==''){
     alert('The chol is required');
     return;
  }


  $.ajax({
      url: "http://localhost:5000/check",
      type: "POST",
      data: {
        trestbps, chol, thalach,  oldpeal, sex,
        chestpain, fbs, R_ECG, angina, slop,
        ca, age
      },
      //data: checkValues,
      success: function (data) {
        console.log(data)
      },
      error: function (err) {
        console.error(err);
      }
  });

});
})

$("#submit").click(function(e) {
    alert("i got clicked")
})