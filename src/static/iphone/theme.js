var theme = 'iphone';

/*
var playlist_item_template_html = "<tr id=\"playlist_item_#{tracklistindex}\"  class=\"playlist_item #{row_class_addon}\"><td><img onclick=\"play_from_list(#{tracklistindex})\" class=\"action\" src=\"" 
									+ theme + "/images/playlist_play.png\" /><img onclick=\"delete_from_list(#{tracklistindex})\" class=\"action\" src=\""
									+ theme + "/images/playlist_delete.png\" /></td><td><span class=\"title #{class_addon}\">#{title}</span></td><td><span class=\"artist #{class_addon}\">#{artist}</span></td><td<span class=\"album #{class_addon}\">#{album}</span></td></tr>";
*/

var playlist_item_template_html = "<li><a href=''><span class='number'>#{tracklistindex}</span><span class='name'>#{artist}</span>&nbsp;<span class='name'>#{album}</span>&nbsp;<span class='name'>#{title}</span></a></li>"

var searchresult_item_template_html = "";