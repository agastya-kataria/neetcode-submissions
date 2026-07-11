class Solution {
    public boolean isPalindrome(String s) {
        if (s.length() == 0) return true;

        int l = 0;
        int r = s.length()-1;
       

        while(r>=l){

            while (!Character.isLetterOrDigit(s.charAt(l)) && l<r) l++;
            while (!Character.isLetterOrDigit(s.charAt(r)) && l<r) r--;
           if(r>=l && Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) return false;

            l++;
            r--;
        }
        return true;
    }
}
