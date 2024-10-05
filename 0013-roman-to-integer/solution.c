int romanToInt(char* s) {
    int total = 0, current = 0, prev = 0;
    
    while (*s) {
        switch (*s) {
            case 'I': current = 1; break;
            case 'V': current = 5; break;
            case 'X': current = 10; break;
            case 'L': current = 50; break;
            case 'C': current = 100; break;
            case 'D': current = 500; break;
            case 'M': current = 1000; break;
        }
        
        total += (current > prev) ? (current - 2 * prev) : current;
        prev = current;
        s++;
    }
    return total;
}
