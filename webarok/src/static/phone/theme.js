var theme = 'phone';

var playlist_item_template_html = "<tr id=\"playlist_item_#{tracklistindex}\"  class=\"playlist_item #{row_class_addon}\" ondblclick=\"play_from_list(#{tracklistindex})\"><td class=\"artisttd\"><span class=\"artist #{class_addon}\">#{artist}</span></td><td class=\"titletd\"><span class=\"title #{class_addon}\">#{title}</span></td><td class=\"actiontd\"><img onclick=\"delete_from_list(#{tracklistindex})\" src=\"phone/images/down.png\" width=\"16\" height=\"16\" class=\"action\" /></td></tr>";
var searchresult_item_template_html = "<tr id=\"search_result_#{url}\"  class=\"playlist_item #{row_class_addon}\" ondblclick=\"playElement(#{url})\"><td class=\"artisttd\"><span class=\"artist #{class_addon}\">#{artist}</span></td><td class=\"titletd\"><span class=\"title #{class_addon}\">#{title}</span></td><td class=\"actiontd\"><img onclick=\"collectionPutElementInTrackList(#{url})\" src=\"phone/images/up.png\" width=\"16\" height=\"16\" class=\"action\" /></td></tr>";

