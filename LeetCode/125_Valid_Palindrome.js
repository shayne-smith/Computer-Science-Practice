var isPalindrome = function(s) {
    // remove space
    let stripped = s.replace(/\s+/g, '');
    
    // remove punctuation
    stripped = stripped.replace(/[.,:%^*@;#\-_?!'`"{()}\[\]]/g, '');
    
    // lowercase letters
    const lowered = stripped.toLowerCase();
    
    // flip string
    const flipped = lowered.split("").reverse().join("");

    console.log(lowered);
    return flipped == lowered;
};