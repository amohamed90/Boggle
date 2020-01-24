let played_words = new Set();

$(function() {
  $(".btn").on("click", function(event) {
    handleClick(event);
  })
})

async function handleClick(event) {
  event.preventDefault();
  let word = $("#word").val().toLowerCase();

  if (played_words.has(word)) {
    // this word has ben played before
  } else {
      // post to our submit route get back the status of the word
    let response = (await axios.post('/submit', {"word": word})).data;
    console.log(response);
      // post message accordingly
    // add word to ul if valid
    // update score with length of word

  }

}

// function showMessage(msg, cls) {

// }

// function 

