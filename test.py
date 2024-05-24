# import json

# def get_top_10_tf_results():
#     # Load the JSON data from the file
#     with open("database.json", "r") as file:
#         data = json.load(file)

#     # Initialize a list to store the top 10 results
#     top_10_results = []

#     # Iterate over each score category for the TF quiz
#     for score_category, results in data["tf"].items():
#         # Iterate over each result in the score category
#         for result in results:
#             # Get the user name, score, and time taken
#             user_name, score, time_taken = result

#             # Convert time taken to an integer for comparison
#             time_taken = int(time_taken)

#             # If the top 10 list is not full yet, or if this result has a better time than the worst result in the list
#             if len(top_10_results) < 10 or time_taken < int(top_10_results[-1][2]):
#                 # Add this result to the top 10 list
#                 top_10_results.append([user_name, score, str(time_taken)])
#                 # Sort the top 10 list by time taken (ascending order)
#                 top_10_results.sort(key=lambda x: int(x[2]))

#                 # Keep only the top 10 results
#                 top_10_results = top_10_results[:10]

#     return top_10_results

# # Example usage:
# top_10_tf_results = get_top_10_tf_results()
# print("Top 10 TF Quiz Results:")
# for result in top_10_tf_results:
#     print(result)


import json

# def get_top_10_tf_results():
#     # Load the JSON data from the file
#     with open("database.json", "r") as file:
#         data = json.load(file)

#     # Initialize a list to collect all results
#     all_results = []

#     # Iterate over each score category for the TF quiz and collect results
#     for score_category, results in data["mcq"].items():
#         all_results.extend(results)

#     # Sort the collected results first by score (descending) and then by time taken (ascending)
#     all_results.sort(key=lambda x: (-int(x[1].split('/')[0]), float(x[2])))

#     # Return the top 10 results
#     return all_results[:10]

# # Example usage:
# top_10_tf_results = get_top_10_tf_results()
# print("Top 10 TF Quiz Results:")
# for result in top_10_tf_results:
#     print(result)
