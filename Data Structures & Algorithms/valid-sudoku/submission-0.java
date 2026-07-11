class Solution {
    public boolean isValidSudoku(char[][] board) {
        int N=9;

        HashSet<Character>[] r = new HashSet[N];
        HashSet<Character>[] c = new HashSet[N];
        HashSet<Character>[] b = new HashSet[N];

        for (int i = 0; i<N; i++)
        {
            r[i] = new HashSet<Character>();
            c[i] = new HashSet<Character>();
            b[i] = new HashSet<Character>();
        }

        for (int i = 0; i< N; i++)
        {
            for (int j = 0; j< N; j++)
            {
                char val = board[i][j];

                if (val == '.') continue;

                if (r[i].contains(val)) return false;
                r[i].add(val);

                if (c[j].contains(val)) return false;
                c[j].add(val);

                int idx = (i/3)*3+(j/3);
                if (b[idx].contains(val)) return false;
                b[idx].add(val);


            }
        }
        return true;
        
    }
}
