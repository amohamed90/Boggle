let played_words = Set();

async function handleClick(event) {
  event.preventDefault();
  let word = $("#word").val();

  if (played_words.has(word)) {
    // this word has ben played before
  } else {
    // post to our submit rout
  }

}
