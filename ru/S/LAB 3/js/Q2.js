function convertWordToPigLatin(word) {
    
  
    return word.substr(1) + word.charAt(0) + 'ay';
  }
  
  function convertPhraseToPigLatin(phrase) {
    const words = phrase.split(' ');
    const pigLatinWords = words.map(word => convertWordToPigLatin(word));
    return pigLatinWords.join(' ');
  }
  
  
  function convertPhrase(event) {
    event.preventDefault();
    const phraseInput = document.getElementById('phrase');
    const convertedTextArea = document.getElementById('converted');
    const phrase = phraseInput.value;
    const convertedPhrase = convertPhraseToPigLatin(phrase);
    convertedTextArea.value += convertedPhrase + '\n';
    phraseInput.value = '';
  }
  