
def failed_entries(logs):
   failed = []
   for log in logs:
     new_log = log.split(" ")
     loggg = new_log[5]

     if loggg == "FAILED":
       failed.append(log)
   return failed

def runtime(logs):
   total = 0
   count = 0
   for log in logs:
     new_log = log.split(" ")
     count += 1
     loggg = new_log[8]
     new_loggg = loggg[:-1]
     total += int(new_loggg)
   average = total / count
   return average

def script_f(logs):
   counts = {}
   failed = failed_entries(logs)
   for fail in failed:
     new_fail = fail.split(" ")
     name = new_fail[3]
     if name in counts:
       counts[name] += 1
     else :
       counts[name] = 1
   highest_v = max(counts, key = counts.get)
   return highest_v


log1 = "2026-03-20 08:00:01 - mysript.sh - SUCCESS - runtime: 2s"
log2 = "2026-03-20 09:00:01 - mysript.sh - FAILED - runtime: 0s"
log3 = "2026-03-20 10:00:01 - backup.sh - FAILED - runtime: 5s"
log4 = "2026-03-20 11:00:01 - mysript.sh - SUCCESS - runtime: 6s"
log5 = "2026-03-20 12:00:01 - mysript.sh - FAILED - runtime: 9s"
log6 = "2026-03-20 01:00:01 - backup.sh - SUCCESS - runtime: 2s"
log7 = "2026-03-20 02:00:01 - mysript.sh - FAILED - runtime: 1s"
log8 = "2026-03-20 03:00:01 - backup.sh - SUCCESS - runtime: 5s"

logs = [log1, log2, log3, log4, log5, log6, log7, log8]


print(f"THE FAILED ENTRIES INCLUDE: { failed_entries(logs)}")
print(f"THE AVERAGE LOGTIME IS: {runtime(logs)}")
print(f"THE SCRIPT WITH THE HIGHEST AMOUNT OF FAILED LOG IS: {script_f(logs)}")
