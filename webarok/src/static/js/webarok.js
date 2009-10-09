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
	player_status_refresher = new PeriodicalExecuter( refreshPlayerStatus, 10 );
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
			$('control_pause').style.display = 'none';
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
var current_song_refresher; 
startRefreshingCurrentSong();

function refreshCurrentSong() {
	callWebarokWithReturn( 'CurrentSong', 'repaintCurrentSong' );
}
function startRefreshingCurrentSong() {
	try {
		current_song_refresher.stop();
		current_song_refresher = null;
	} catch ( e ) {}
	current_song_refresher = new PeriodicalExecuter( refreshCurrentSong, 5 );
}
function toggleRefreshCurrentSong( value ) {
	if (value)	startRefreshingCurrentSong();
	else		current_song_refresher.stop();
}
function repaintCurrentSong( data )
{
	song_length = data['mtime'];
	song_position = data['position'];
	if ( current_song_tracklist_index != data['tracklistindex'] )
	{
		refreshPlaylist();
	}
	
	data['duration_min'] = Math.floor( data['time'] / 60 );
	data['duration_sec'] = Math.floor(((data['time'] / 60) - data['duration_min']) * 60); 

	repaint( data );
	repaintCurrentPosition( data ); 
	try	{
		$('albumart').src = '/action/Art/' + data['albumartremoteurl'];
	}	catch( e ) {}
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
	playlist_refresher = new PeriodicalExecuter( refreshPlaylist, 5 );
} 
function toggleRefreshPlaylist( value ) {
	if (value) 	startRefreshingPlaylist();
	else		playlist_refresher.stop();
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
	$('playlist').innerHTML = '<table>' + playlist + '</table>';
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
		current_song_refresher.stop();
		volume_refresher = null;
	} catch ( e ) {}
	volume_refresher = new PeriodicalExecuter( refreshVolume, 60 );
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
function repaintCurrentPosition()
{
	if ( song_length == 0 ) return;
	//$( 'progress_foreground' ).style.width = (( song_position/song_length ) * 100) + '%'; 
	progress_bar.setProgress( ( song_position/song_length ) * 100 );
	
	
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
//******* End: basic functions