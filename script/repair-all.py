import os

bug_path = "/tmp/RSRepair_QuixBugs_DEPTH_FIRST_SEARCH_"

result = {
                "patches": []
            }

output_folder = None
for d in os.listdir(bug_path):
    if "patches_" in d:
        output_folder = d
        break

path_results = os.path.join(bug_path, output_folder)
if os.path.exists(path_results):
    for f in os.listdir(path_results):
        path_f = os.path.join(path_results, f)
        if not os.path.isfile(path_f) or ".txt" not in f:
            continue
        with open(path_f) as fd:
            str_patches = fd.read().split(
                "**************************************************")
            edits = []
            for str_patch in str_patches:
                splitted_patch = str_patch.strip().split("\n")
                info_line = splitted_patch[0].split(" ")
                if info_line[0] == "Evaluations:" or "EstimatedTime:" == info_line[0]:
                    continue

                is_kali = "." in info_line[-1]
                if not is_kali:
                    edit = {
                        "type": info_line[1],
                        "path": " ".join(info_line[2:-1]).replace("%s/" % bug_path, ""),
                        "line": int(info_line[-1])
                    }
                    content = "%s\n" % splitted_patch[2]
                    for line in splitted_patch[3:]:
                        if line == "Seed:":
                            edit["faulty"] = content.strip()
                            content = ""
                        else:
                            content += "%s\n" % line
                    edit["seed"] = content.strip()
                else:
                    edit = {
                        "type": "%s %s" % (info_line[0], info_line[1]),
                        "path": " ".join(info_line[2:-2]).replace("%s/" % bug_path, ""),
                        "line": int(info_line[-2]),
                        "faulty": "\n".join(splitted_patch[1:])
                    }

                edits.append(edit)
            result["patches"].append({
                "edits": edits
            })
    print result