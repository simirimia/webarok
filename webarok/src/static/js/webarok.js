var song_length = 0;
var song_position = 0;

 

//******* Start: Player status handling
var player_status_refresher;
startRefreshingPlayerStatus();

function refreshPlayerStatus() {
	callWebarokWithReturn( 'PlayerStatus', 'repaintPlayerStatus' );
}
function startRefreshingPlayerStatus() {
	try{
		player_status_refresher.stop();
		player_status_refresher = null;
	} catch ( e ) {}
	try	{
		var rate = parseFloat($('refresh_rate_playerstatus').value);
		if ( isNaN(rate) ) {
			rate = 10;
		}
	}
	catch( e )	{
		rate = 10;
	}
	player_status_refresher = new PeriodicalExecuter( refreshPlayerStatus, rate );
}
function toggleRefreshPlayerStatus( value )  {
	if (value)  startRefreshingPlayerStatus();
	else		player_status_refresher.stop();
}
function repaintPlayerStatus( data )
{
	repaint( data );
	switch( data['status'] )
	{
		case 'stopped':
			$('control_stop').style.display = 'none';
			$('control_pause').style.display = '';
			$('control_play').style.display = '';
			toggleRefreshProgress( false );
			toggleRefreshCurrentSong( false );
			break;
		case 'paused':
			$('control_stop').style.display = '';
			// VLC expects a pause in paused mode
			// Amarok expects a play in paused mode
			//$('control_pause').style.display = 'none';
			$('control_pause').style.display = '';
			$('control_play').style.display = '';
			toggleRefreshProgress( false );
			toggleRefreshCurrentSong( false );
			break;
		case 'playing':
			$('control_stop').style.display = '';
			$('control_pause').style.display = '';
			$('control_play').style.display = 'none';
			if ( $('check_refresh_progress').checked ) {
				toggleRefreshProgress( true );
			}
			if ( $('check_refresh_song').checked ) {
				toggleRefreshCurrentSong( true );
			}
			break;
	} 
}
//******* End: Player status handling

//******* Start: Current Song handling

//To prevent refresing the same data:
var currentsong = "";
var current_song_refresher; 
startRefreshingCurrentSong();

function refreshCurrentSong( all ) {
	callWebarokWithReturn( 'CurrentSong', 'repaintCurrentSong' );
	if ( all == 1 ){
	
		currentsong = "";
	}
}
function startRefreshingCurrentSong() {
	try {
		current_song_refresher.stop();
		current_song_refresher = null;
	} catch ( e ) {}
	
	try	{
		var rate = parseFloat($('refresh_rate_song').value);
		if ( isNaN(rate) ) {
			rate = 10;
		}
	}
	catch( e )	{
		rate = 10;
	}
	
	current_song_refresher = new PeriodicalExecuter( refreshCurrentSong, rate );
}
function toggleRefreshCurrentSong( value ) {
	if (value)	startRefreshingCurrentSong();
	else		current_song_refresher.stop();
}


function repaintCurrentSong( data )
{
	if (data['lyrics']!=""){
	data['lyrics'] = nl2br(data['lyrics']);
	}else{
	data['lyrics'] = "No Lyrics found. (Click to refresh)"
	}
	song_length = data['mtime'];
	song_position = data['position'];
	data['position_in_secs'] = data['position'] / 1000;
	data['position_min'] = Math.floor( data['position_in_secs'] / 60 );
	data['position_sec'] = Math.floor(((data['position_in_secs'] / 60) - data['position_min']) * 60); 
	if( data['position_sec'] < 10 ) data['position_sec'] = '0' + data['position_sec']; 
	
	if (currentsong!=(data['title']+data['artist']+data['album']+data['mtime'])){
	currentsong = (data['title']+data['artist']+data['album']+data['mtime']);
	//window.status = currentsong;
	$$( '#playlist span.current'  ).each( function(e){ e.removeClassName( 'current' ) } );
	$$( '.current_playlist_item' ).each( function(e){ e.removeClassName( 'current_playlist_item' ); } );
	
	try {
		$('playlist_item_' + data['tracklistindex'] ).addClassName( 'current_playlist_item' );
	}
	catch( e ) {}
	
	try {
		$$( '#playlist_item_' + data['tracklistindex'] + ' span' ).each( function(e){ e.addClassName( 'current' ) } );
	}
	catch( e ) {}
	
	data['duration_min'] = Math.floor( data['time'] / 60 );
	data['duration_sec'] = Math.floor(((data['time'] / 60) - data['duration_min']) * 60); 
	if( data['duration_sec'] < 10 ) data['duration_sec'] = '0' + data['duration_sec'];
	
	
	repaint( data );
	try	{
		$('albumart').src = '/action/Art/' + data['albumartremoteurl'];      
	}	catch( e ) {}
        }
	repaintCurrentPosition( data ); 
} 
//******* End: Current Song handling

//******* Start: Playlist handling

var playlist_refresher;

// only refresh playlist once
// startRefreshingPlaylist();
refreshPlaylist();

function refreshPlaylist() {
	try
	{
		$('playlist_spinner').show();
		$('playlist').hide();
	}
	catch ( e ) {}
	
	
	
	callWebarokWithReturn( 'TrackListGet', 'repaintPlaylist' ); 
	
	try
	{
		$('playlist').show();
		$('playlist_spinner').hide();
	}
	catch ( e ) {}
	
}
function startRefreshingPlaylist() {
	
	try {
		playlist_refresher.stop();
		playlist_refresher = null;
	} catch ( e ) {}
	
	try	{
		var rate = parseFloat($('refresh_rate_playlist').value);
		if ( isNaN(rate) ) {
			rate = 300;
		}
	}
	catch( e )	{
		rate = 300;
	}
	
	
	playlist_refresher = new PeriodicalExecuter( refreshPlaylist, rate );
} 
function toggleRefreshPlaylist( value ) {
	if (value) 	startRefreshingPlaylist();
	else {
		try {
			playlist_refresher.stop();
		}
		catch( e ) {}
	}
}

var playlist_item_template = new Template( playlist_item_template_html );
var current_song_tracklist_index = 0;
function repaintPlaylist( data ) {
	var playlist = '';
	data.each(  function(conv){
		if (conv.is_current == true)
		{
			conv.class_addon = 'current';
			conv.row_class_addon = 'current_playlist_item';
			current_song_tracklist_index = conv.tracklistindex;
		}
		playlist = playlist + playlist_item_template.evaluate(conv);
	});
	$('playlist').innerHTML = '<table><tr><th>Interpret</th><th>Titel</th></tr>' + playlist + '</table>';
}

function play_from_list( index )
{
	callWebarok( 'TrackListPlayElement/' + index );
	refreshPlaylist();
}

function delete_from_list( index )
{
	callWebarok( 'TrackListDeleteElement/' + index );
	refreshPlaylist();
}
//******* End: Playlist handling

//******* Start: Volume handling

var volume_refresher;
startRefreshingVolume();

function refreshVolume() {
	callWebarokWithReturn( 'VolumeGet', 'repaintVolume' );
}
function startRefreshingVolume() {
	try {
		volume_refresher.stop();
		volume_refresher = null;
	} catch ( e ) {}
	
	try	{
		var rate = parseFloat($('refresh_rate_volume').value);
		if ( isNaN(rate) ) {
			rate = 60;
		}
	}
	catch( e )	{
		rate = 60;
	}
	
	volume_refresher = new PeriodicalExecuter( refreshVolume, rate );
}
function toggleRefreshVolume( value ) {
	if (value)	startRefreshingVolume();
	else		volume_refresher.stop();
}
function repaintVolume( data )
{
	repaint( data );
} 
//******* End: Volume handling



//******* Start: Position handling
// partly integrated in current song handling
function repaintCurrentPosition( data )
{
	if ( song_length == 0 ) return;
	//$( 'progress_foreground' ).style.width = (( song_position/song_length ) * 100) + '%'; 
	progress_bar.setProgress( ( song_position/song_length ) * 100 );
	$('position_min').innerHTML = data['position_min'];
	$('position_sec').innerHTML = data['position_sec'];
	
	/*
	var data = $H();
	data['position_min'] = Math.floor( song_position / 60000 );
	data['position_sec'] = ((song_length / 60000) - data['position_min']) * 60;
	repaint( data ); 
	*/
} 

var progress_bar_refresher;
startRefreshProgressBar();
function startRefreshProgressBar()
{
/*
	try {
		current_song_refresher.stop();
		progress_bar_refresher = null;
	} catch ( e ) {}
	progress_bar_refresher = new PeriodicalExecuter( intermidiateProgressBarUpdate, 1 );
*/
}
function intermidiateProgressBarUpdate()
{
	$('debug').innerHTML = $('debug').innerHTML + '*'; 
	song_position = song_position + 1000;
	repaintCurrentPosition();
}
function toggleRefreshProgress( value ) {
	if (value)	{
		startRefreshProgressBar();
		$('current_position').style.display = 'block';
	} else {
		progress_bar_refresher.stop();
		$('current_position').style.display = 'none';
	}
	
}

//******* End: Position handling

//******* Start: convinience functions
function doAfterPlayerAction()
{
	refreshCurrentSong();
	refreshPlayerStatus();
	refreshPlaylist();
}
//******* Start: convinience functions


//******* Start: basic functions

function repaint( data ) {
	for( thekey in data )
	{
		try
		{
			$(thekey).innerHTML = data[thekey];
		}
		catch( e ) {}
	} 
}

function callWebarokWithReturn( action, doOnSuccess )
{
	new Ajax.Request( '/action/' + action,
	{
	    method:'get',
	    onSuccess: function(transport) { eval( doOnSuccess + '(transport.responseText.evalJSON( true ))' ); },
	    onFailure: function(){ alert('Something went wrong...') }
	});

}
function callWebarok( action, doOnSuccess )
{
	new Ajax.Request( '/action/' + action,
	{
	    method:'get',
	    onSuccess: eval( doOnSuccess ),
	    onFailure: function(){ alert('Something went wrong...') }
	});

}

//http://snipplr.com/view/634/replace-newlines-with-br-platform-safe/
function nl2br(text){
	text = escape(text);
	if(text.indexOf('%0D%0A') > -1){
	    re_nlchar = /%0D%0A/g ;
	}else if(text.indexOf('%0A') > -1){
	    re_nlchar = /%0A/g ;
	}else if(text.indexOf('%0D') > -1){
	    re_nlchar = /%0D/g ;
	}
	return unescape( text.replace(re_nlchar,'<br />') );
}
//******* End: basic functions

//******* Start: Search handling

function collectionSearchAll() {
	try
	{
		$('searchresults').hide();
	}
	catch ( e ) {}
	
	
	callWebarokWithReturn( 'Search'+$F('searchtags')+'/'+$F('searchterm'), 'repaintSearchResults' ); 
	
	try
	{
		$('searchresults').show();
	}
	catch ( e ) {}
	
}

var searchresult_item_template = new Template( searchresult_item_template_html );
function repaintSearchResults( data ) {
	var searchresults = '';
	data.each(  function(conv){
		searchresults = searchresults + searchresult_item_template.evaluate(conv);
	});
	$('searchresults').innerHTML = '<table><tr><th>Interpret</th><th>Titel</th></tr>' + searchresults + '</table>';
}

function playElement( url )
{
	callWebarok( 'SearchPlayElement/' + url );
	refreshPlaylist();
}

function collectionPutElementInTrackList( url )
{
	callWebarok( 'SearchPutElementToTrackList/' + url );
	refreshPlaylist();
	$('search_result_' + url).addClassName("inPlaylist");
}
//******* End: Search handling



//******* Start: Seek handling

// For seeking with the progressbar only

function seek(e) {
	var xPos = Event.pointerX(e);
	xPos = xPos-10;
	percent = xPos*100.0/285.0;
        //alert (percent);
	callWebarok( 'Seek/' + percent );
	refreshCurrentSong();
}
//******* End: Seek handling