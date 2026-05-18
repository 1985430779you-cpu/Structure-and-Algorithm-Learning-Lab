class Solution:
    def calc_amount(self, pairs, rates, initialCurrency):
        from collections import defaultdict
        g = defaultdict(list)
        for (x, y), r in zip(pairs, rates):
            g[x].append((y, r))
            g[y].append((x, 1.0 / r))

        amount = {}
        def dfs(x: str, cur_amount: float) -> None:
            amount[x] = cur_amount
            for to, rate in g[x]:
                if to not in amount:
                    dfs(to, cur_amount * rate)
        dfs(initialCurrency, 1.0)
        return amount

    def maxAmount(self, initialCurrency, pairs1, rates1, pairs2, rates2):
        day1_amount = self.calc_amount(pairs1, rates1, initialCurrency)
        day2_amount = self.calc_amount(pairs2, rates2, initialCurrency)
        return max(day1_amount.get(x, 0.0) / a2 for x, a2 in day2_amount.items())

initialCurrency = "EUR"
pairs1 = [["EUR","USD"],["USD","JPY"]] 
rates1 = [2.0,3.0]
pairs2 = [["JPY","USD"],["USD","CHF"],["CHF","EUR"]]
rates2 = [4.0,5.0,6.0]
print(Solution().maxAmount(initialCurrency, pairs1, rates1, pairs2, rates2))   