class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int count = 0;

        map<char, int> mapStones;

        for (auto s : stones) {
            mapStones[s]++;
        }

        for (auto j : jewels) {
            count += mapStones[j];
        }

        return count;
    }
};
