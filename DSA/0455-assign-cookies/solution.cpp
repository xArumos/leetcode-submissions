class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        if (!s.size()) {
            return 0;
        }
        if (!g.size()) {
            return 0;
        }
        int count = 0;
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int j=0;
        for(int i=0; i < s.size(); i++) {
            if (j < g.size() && g[j] <= s[i]) {
                count++;
                j++;
            }
        }
        return count;
        
    }
};
