class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> letters;
        for (auto i : s) {
            letters[i]++;
        }
        for (auto j : t) {
            letters[j]--;
        }

        for (auto x : letters) {
            if (x.second != 0) {
                return false;
            }
        }

        return true;
    }
};
