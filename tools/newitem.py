# add a new project page to website
# can be in one of the five categories
# Herminio Gonzalez, March 2020

# these are the five different categories of projects
CategoriesMap = {
    "gov_manage": "官公庁管理",
    "gov_const": "官公庁工事",
    "pri_manage": "民間管理",
    "pri_const": "民間工事",
    "other": "その他作業"
}

# template for new entry in one of the listing pages
NewEntry = '''
						<li>
							<div class="left imagelinksmall">
								<p><a href="TTTprojPage"><img width="222" height="155" src="TTTThumb" class="attachment-thumbnail wp-post-image" alt="スタジオ縁 造園 緑化 整備" /></a></p>
							</div>
							<div class="right">
								<div>
									<p class="archiveNote">
										<span><img class="opacity" src="img/works/telus-link-icon.png" alt="スタジオ縁 造園 緑化 整備" />
										</span>TTTCategory
									</p>
									<p class="archiveTitle"><a href="TTTprojPage">TTTCaption</a></p>
								</div>
							</div>
						</li>
'''


# here are your parameters
theCaption = "R2年・市道45-022号線舗装修繕工事"
seed = "gov_const"
idx = "35"             # the next number in the series of works.
thumb = "thumb"        # image file for thumbnail, sans extension.

# massage parameters
theListingFile = "works_" + seed + ".html"
theCategory = CategoriesMap[seed]
theProjPage = "work_" + seed + idx +".html"
theThumb = "img/work_" + seed + idx + "/" + thumb + ".jpg"

# prepare new <li> tag (T-T-T-tag:)
entry = NewEntry.replace('TTTCategory', theCategory)
entry = entry.replace('TTTprojPage', theProjPage)
entry = entry.replace('TTTThumb', theThumb)
entry = entry.replace('TTTCaption', theCaption)


f = open(theListingFile, 'r', encoding="utf-8")
text = f.read()

# insert new <li> tag
(head, tag, tail) = text.partition('<!--newitem-->')
if tag == "": 
    print("Error: tag not found.")
    exit()

text2 = head + tag + entry + tail

# overwrite listing file with new stuff
f.close()
f2 = open(theListingFile, 'w', encoding="utf-8")
f2.write(text2)
f2.close()

print("finished.")
exit(0)

