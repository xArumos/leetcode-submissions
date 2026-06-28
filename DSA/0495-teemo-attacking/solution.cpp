class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int count = 0;
        if (timeSeries.size() == 1) {
            count += duration;
            return count;
        } else {
            for (int i = 0; i < timeSeries.size() - 1; i++) {
                if (timeSeries[i] - 1 + duration < timeSeries[i + 1]) {
                    count += duration;
                } else {
                    count += timeSeries[i + 1] - timeSeries[i];
                }
            }

            count += duration;
            
            return count;
        }
    }
};
