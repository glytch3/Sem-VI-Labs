
function generateWords() {
    const wordInput = document.getElementById('word');
    const outputTextArea = document.getElementById('output');
    const word = wordInput.value.toLowerCase();
    const words = [];
    for (let i = 0; i < 5; i++) {
      for (let j = 0; j < 5; j++) {
        for (let k = 0; k < 5; k++) {
            if (i != j && i != k && j != k ) {
          const threeLetterWord = word[i] + word[j] + word[k];
          words.push(threeLetterWord);
            }
        }
      }
    }
  
    outputTextArea.value = words.join('\n');
  }
  
  