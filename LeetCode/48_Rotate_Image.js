var rotate = function(matrix) {
    
    const transpose = (matrix) => {
        const n = matrix.length;
        // nested for loops
        for (let i=0; i < n; i++) {
            for (let j=i; j < n; j++) {
                let tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            };
        };
    };
    
    const reflect = (matrix) => {
        n = matrix.length;
        for (let i=0; i < n; i++) {
            for (let j=0; j < Math.floor(n/2); j++) {
                let tmp = matrix[i][j];
                
            };
        };
        // nested for loops
            // i values stay constant
            // j values transform to (n - 1 - j)
                // matrix[i][j] = matrix
    };
    
    transpose(matrix);
    reflect(matrix);  
};
