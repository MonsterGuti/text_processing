title = input()
content = input()

print(f"<h1>\n\t{title}\n</h1>")
print(f"<article>\n\t{content}\n</article>")

number_of_comments = 0
while True:
    comment = input()
    if comment == "end of comments":
        break
    print(f"<div>\n\t{comment}\n</div>")
