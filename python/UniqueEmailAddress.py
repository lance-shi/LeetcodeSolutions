# Question No. 929
# Unique Email Addresses
class Solution:
    def numUniqueEmails(self, emails):
        d = Counter()
        for mail in emails:
            local, domain = mail.split("@")
            local = local.replace(".", "")
            if "+" in local: local = local[:local.index("+")]
            d[local + "@" + domain] += 1
            
        return len(d)