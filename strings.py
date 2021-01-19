class Solution:
    def removeVowels(self, S):
        new_s = ''
        for ch in S:
            if ch not in "aeiou":
                new_s = new_s + ch
        return new_s
    def numUniqueEmails(self, emails):
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)

#Задачка с разворотом строки
s = ["1", "2", "3", "4", "5"]
if not s:
    print("schade")
left = 0
right = len(s) - 1
print("right ", right)
while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
print (s)
