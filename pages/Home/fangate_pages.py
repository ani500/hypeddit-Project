import time
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as c1
import logging
from pages.Home.locators import Locators
from pages.Home.login_pages import LoginPage



class FangatePage(SeleniumDriver):
    log = c1.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    # Locators

    _dev_unlock_password = "//form[@id='devlock']//input[@type='password']"
    _dev_unlock_button = "//div[@class='form-group']//button[@type='submit']"
    _login_link = "Login"
    _email_field = "login_email"
    _password_field = "login_password"
    _login_button = "login_button"
    _stats_visits = "stats_visit_total"
    # Locators Fangate
    _share_music_link = "Share Music"
    _download_gate_button = "//a[@href='https://hypeddit.com/gate/create']"
    _link_gate_button = "//a[@href='https://hypeddit.com/gate/create/url']"
    # source Section
    _track_url = "track_url"
    _source_next_button = "next_box_button_source"
    # Genre Section
    _genre_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Select genre']"
    _select_genre = "//ul[@class='dropdown-menu inner']//span[text()='Bass']"
    _genre_next_button = "next_box_button_genre"
    # Upload Section
    _choose_file = "inputFilemp3"
    _upload_next_button = "next_box_button_upload"
    # Title Section
    _artist_name = "artist_name"
    _track_title = "track_title"
    
    _title_next_button = "next_box_button_title"
    # Design Section
    _upload_coverart_button = "selectManualCoverart"
    _dark_theme_radio_button =  "//div[@class='checkbox']//label[@for='dark_theme']"
    _design_next_button = "next_box_button_design"

    # Gate Steps Section
    # -------------------Email------------------

    _add_email_step = "add_email_button"
    _collect_email_id = "collect_email"
    _collect_email = "//div[@class='checkbox']//label[@for='collect_email']"
    _collect_email_names_id = "collect_email_names"
    _collect_email_names = "//div[@class='checkbox']//label[@for='collect_email_names']"
    _skippable_email_id = "skippable_email"
    _skippable_email = "//div[@class='checkbox']//label[@for='skippable_email']"

    # -------------------Soundcloud------------------

    _add_soundcloud_step = "add_soundcloud_button"
    _follow_profile = "//div[@class='checkbox']//label[@for='follow_sc']"
    _follow_sc_id = "follow_sc"
    _comment_sc = "//div[@class='checkbox']//label[@for='comment_sc']"
    _comment_sc_id = 'comment_sc'
    _like_sc = "//div[@class='checkbox']//label[@for='like_sc']"
    _like_sc_id = "like_sc"
    _repost_sc = "//div[@class='checkbox']//label[@for='repost_sc']"
    _repost_sc_id = "repost_sc"
    _skippable_sc = "//div[@class='checkbox']//label[@for='skippable_sc']"
    _skippable_sc_id = "skippable_sc"
    _add_scoundcloud_artist = "add_soundcloud_artist"
    _add_soundcloud_track = "add_soundcloud_track"
    _gate_step_next_button = "next_box_button_gate-steps"

    # -------------------Youtube------------------
    _add_youtube_step = "add_youtube_button"
    _subscribe_yt_id = "subscribe_yt"
    _subscribe_yt = "//div[@class='checkbox']//label[@for='subscribe_yt']"
    _skippable_yt_id = "skippable_yt"
    _skippable_yt = "//div[@class='checkbox']//label[@for='skippable_yt']"
    _add_channel_yt_url = "add_youtube_channel_custom_url"
    _add_channel_yt_name = "add_youtube_channel_custom_name"
    _yt_profile_add_button = "youtube_profile_add_button"
    # ---------------------xxxx------------------------------------------
    # ------------------------Spotify------------------------------------
    _add_spotify_step = "add_spotify_button"
    _follow_sp_id = "follow_sp"
    _follow_sp = "//div[@class='checkbox']//label[@for='follow_sp']"
    _save_sp_id = "save_track_sp"
    _save_sp = "//div[@class='checkbox']//label[@for='save_track_sp']"
    _skippable_sp_id = "skippable_sp"
    _skippable_sp = "//div[@class='checkbox']//label[@for='skippable_sp']"
    _add_artist_sp = "add_spotify_artist"
    _add_track_sp = "add_spotify_track"

    # --------------------------Apple Step-----------------------------------------

    _add_apple_step = "add_apple_button"
    _like_ap_id = "like_ap"
    _like_ap = "//div[@class='checkbox']//label[@for='like_ap']"
    _save_ap_id = "save_track_ap"
    _save_ap = "//div[@class='checkbox']//label[@for='save_track_ap']"
    _skippable_ap_id = "skippable_ap"
    _skippable_ap = "//div[@class='checkbox']//label[@for='skippable_ap']"
    _add_artist_ap = "add_apple_artist"

    # ----------------------------Deezer Step------------------------
    _add_deezer_step = "add_deezer_button"
    _follow_dz_id = "follow_dz"
    _follow_dz = "//div[@class='checkbox']//label[@for='follow_dz']"
    _save_dz_id = "save_track_dz"
    _save_dz = "//div[@class='checkbox']//label[@for='save_track_dz']"
    _skippable_dz_id = "skippable_dz"
    _skippable_dz = "//div[@class='checkbox']//label[@for='skippable_dz']"
    _add_artist_dz = "add_deezer_artist"
    _add_track_dz = "add_deezer_track"

    # ----------------Mixcloud Step------------------------------------

    _add_mixcloud_step = "add_mixcloud_button"
    _follow_mc_id = "follow_mc"
    _follow_mc = "//div[@class='checkbox']//label[@for='follow_mc']"
    _repost_mc_id = "repost_mc"
    _repost_mc = "//div[@class='checkbox']//label[@for='repost_mc']"
    _like_mc_id = "like_mc"
    _like_mc = "//div[@class='checkbox']//label[@for='like_mc']"
    _skippable_mc_id = "skippable_mc"
    _skippable_mc = "//div[@class='checkbox']//label[@for='skippable_mc']"
    _add_artist_mc = "add_mixcloud_artist"
    _add_track_mc = "add_mixcloud_track"

    # -----------------------twitter step--------------------------------

    _add_twitter_step = "add_twitter_button"
    _follow_tw_id = "follow_tw"
    _follow_tw = "//div[@class='checkbox']//label[@for='follow_tw']"
    _share_tw_id = "share_tw"
    _share_tw = "//div[@class='checkbox']//label[@for='share_tw']"
    _skippable_tw_id = "skippable_tw"
    _skippable_tw = "//div[@class='checkbox']//label[@for='skippable_tw']"
    _add_profile_tw = "add_twitter"

    # -----------------------Twitch---------------------------------------

    _add_twitch_step = "add_twitch_button"
    _follow_th_id = "follow_th"
    _follow_th = "//div[@class='checkbox']//label[@for='follow_th']"
    _subscribe_th_id = "subscribe_th"
    _subscribe_th = "//div[@class='checkbox']//label[@for='subscribe_th']"
    _skippable_th_id = "skippable_th"
    _skippable_th = "//div[@class='checkbox']//label[@for='skippable_th']"
    _add_artist_th = "add_twitch_artist"
    # -------------------Messenger Step ----------------------------

    _add_fb_msgr_step = "add_facebook_msgr_button"
    _subscribe_fb_msgr_id = "subscribe_fb_msgr"
    _subscribe_fb_msgr = "//div[@class='checkbox']//label[@for='subscribe_fb_msgr']"
    _skippable_fb_msgr_id = "skippable_fb_msgr"
    _skippable_fb_msgr = "//div[@class='checkbox']//label[@for='skippable_fb_msgr']"
    _chatbot_platform_caret_fb_msgr = "//button[@class='btn dropdown-toggle btn-default']//span[text()='No chatbot selected']"
    _select_chatbot_fb_msgr = "//div[@class='dropdown-menu open']//span[text()='ManyChat']"
    _add_page_fb_msgr = "add_facebook_msgr"

    # --------------------------Facebook step --------------------------------

    _add_facebook_step = "add_facebook_button"
    _share_fb_id = "share_fb"
    _share_fb = "//div[@class='checkbox']//label[@for='share_fb']"
    _like_fb_id = "like_fb"
    _like_fb = "//div[@class='checkbox']//label[@for='like_fb']"
    _skippable_fb_id = "skippable_fb"
    _skippable_fb = "//div[@class='checkbox']//label[@for='skippable_fb']"
    _add_page_fb = "add_facebook"
    # ------------------------------------Instagram step-------------------
    _add_instagram_step = "add_instagram_button"
    _follow_ig_id = "follow_ig"
    _follow_ig = "//div[@class='checkbox']//label[@for='follow_ig']"
    _skippable_ig_id = "skippable_ig"
    _skippable_ig = "//div[@class='checkbox']//label[@for='skippable_ig']"
    _add_profile_ig = "add_instagram"

    # ------------------------------------Tiktok step-------------------
    _add_tiktok_step = "add_tiktok_button"
    _follow_tk_id = "follow_tk"
    _follow_tk = "//div[@class='checkbox']//label[@for='follow_tk']"
    _skippable_tk_id = "skippable_tk"
    _skippable_tk = "//div[@class='checkbox']//label[@for='skippable_tk']"
    _add_profile_tk = "add_tiktok"

    # ------------------------------------Bandcamp step-------------------
    _add_bandcamp_step = "add_bandcamp_button"
    _follow_bc_id = "follow_bc"
    _follow_bc = "//div[@class='checkbox']//label[@for='follow_bc']"
    _skippable_bc_id = "skippable_bc"
    _skippable_bc = "//div[@class='checkbox']//label[@for='skippable_bc']"
    _add_profile_bc = "add_bandcamp"

    # ------------------------------------Donation step-------------------
    _add_donation_step = "add_donation_button"
    _add_donation = "donation_id"

    # ------------------------------------------------------------------------

    # Link Url Section
    _edit_custom_link = "edit_custom_link"
    _page = "custom_link_artist"
    _optional = "custom_link_title"
    _linkUrl_next_button = "next_box_button_linkurl"
    # Release Settings Section
    # Release Settings Section
    _set_newRelease_public = "//div[@class='checkbox']//label[@for='set_newrelease_public']"
    _set_newRelease = "//div[@class='checkbox']//label[@for='set_newrelease']"
    _release_settings_button = "next_box_button_newrelease"
    # Email Promotion Section
    _email_promotion_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Please select music']"
    _select_fangate = "//div[@class='dropdown-menu open']//span[text()='Automatically email my newest download gate']"
    _email_promotion_next_button = "next_box_button_email-promotion"
    # Tracking Pixels Section
    _facebook_pixel = "facebook_pixel"
    _facebook_pixel_token = "facebook_pixel_token"
    _google_pixel = "google_pixel"
    _google_pixel_label = "google_pixel_label"
    _tracking_pixels_next_button = "next_box_button_pixel"
    # Confirmation Section
    _create_fangate_button = "next_box_button_confirmation"

    # -----------------------Link Gate section----------------
    # Title Step
    _link_artist_name = "artist_name"
    _link_title = "track_title"
    _link_titleSection_next_button = "next_box_button_title"

    # Secret Link Step
    _link_custom_redir_url = "custom_redirection_url"
    _link_SecretLink_next_button = "next_box_button_secret-link"
    # Unlock Button Text Step
    _link_button_text_dropdown = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Select button text']"
    _link_menu_select_dropdown = "//div[@class='dropdown-menu open']//span[text()='Download']"
    _link_unlock_button_next_button = "next_box_button_unlock"

    # Design Section
    _choose_coverart = "inputManualCoverart"

    # Confirmation Section Link gate
    _create_linkgate_button = "next_box_button_confirmation"

    # -----------------Smartlink Section ---------------------
    _smartlink_gate_button = "//a[@href='https://hypeddit.com/smartlink/create']"
    _audio_preview_next_button = "next_box_button_audio-preview"

    # Spotify Step

    _save_track_spotify_id = "save_track_spotify"
    _save_track_spotify = "//div[@class='checkbox']//label[@for='save_track_spotify']"

    _email_capture_spotify_id = "email_capture_spotify"
    _email_capture_spotify = "//div[@class='checkbox']//label[@for='email_capture_spotify']"

    _add_to_playlist_spotify_id = "add_to_playlist_spotify"
    _add_to_playlist_spotify = "//div[@class='checkbox']//label[@for='add_to_playlist_spotify']"

    _follow_spotify_smartlink_id = "follow_spotify"
    _follow_spotify_smartlink = "//div[@class='checkbox']//label[@for='follow_spotify']"

    # Apple Step

    _save_track_imusic_id = "save_track_imusic"
    _save_track_imusic = "//div[@class='checkbox']//label[@for='save_track_imusic']"

    _add_to_playlist_imusic_id = "add_to_playlist_imusic"
    _add_to_playlist_imusic = "//div[@class='checkbox']//label[@for='add_to_playlist_imusic']"

    _follow_imusic_id = "follow_imusic"
    _follow_imusic = "//div[@class='checkbox']//label[@for='follow_imusic']"

    # Deezer Section

    _save_track_deezer_id = "save_track_deezer"
    _save_track_deezer = "//div[@class='checkbox']//label[@for='save_track_deezer']"

    _email_capture_deezer_id = "email_capture_deezer"
    _email_capture_deezer = "//div[@class='checkbox']//label[@for='email_capture_deezer']"

    _add_to_playlist_deezer_id = "add_to_playlist_deezer"
    _add_to_playlist_deezer = "//div[@class='checkbox']//label[@for='add_to_playlist_deezer']"

    _follow_deezer_smartlink_id = "follow_deezer"
    _follow_deezer_smartlink = "//div[@class='checkbox']//label[@for='follow_deezer']"

    # youtube Step
    _add_link_url_new18_yt = "add_link_url_new18"

    _add_youtubemusic_button = "add_youtubemusic_button"
    _add_link_url_new19_ytmusic = "add_link_url_new19"

    _add_amazon_button = "add_amazon_button"
    _add_link_url_new20_amazon = "add_link_url_new20"

    _add_amazonmusic_button = "add_amazonmusic_button"
    _add_link_url_new21_amzmusic = "add_link_url_new21"

    _add_google_button = "add_google_button"
    _add_link_url_new22_google = "add_link_url_new22"

    _add_googleplay_button = "add_googleplay_button"
    _add_link_url_new23_googleplay = "add_link_url_new23"

    _add_beatport_button = "add_beatport_button"
    _add_link_url_new24_beatport = "add_link_url_new24"

    _add_tidal_button = "add_tidal_button"
    _add_link_url_new25_tidal = "add_link_url_new25"

    _add_pandora_button = "add_pandora_button"
    _add_link_url_new26_pandora = "add_link_url_new26"

    _add_yandex_button = "add_yandex_button"
    _add_link_url_new27_yandex = "add_link_url_new27"

    _add_hypeddit_button = "add_hypeddit_button"
    _add_link_url_new28_hypeddit = "//input[@data-type='hypeddit' and @type='text']"

    _add_bandcamp_button = "add_bandcamp_button"
    _add_link_url_new29_bandcamp = "add_link_url_new29"

    _add_junodownload_button = "add_junodownload_button"
    _add_link_url_new30_junodownload = "add_link_url_new30"

    _add_traxsource_button = "add_traxsource_button"
    _add_link_url_new31_tracksource = "add_link_url_new31"

    _add_tiktok_button = "add_tiktok_button"
    _add_link_url_new32_tiktok = "add_link_url_new32"

    _add_share_button = "add_share_button"

    # Email Capture Section
    _add_fanclub_button = "add_fanclub_button"
    _email_link_id = "email_link"
    _email_link = "//div[@class='checkbox']//label[@for='email_link']"
    _email_exit_id = "email_exit"
    _email_exit = "//div[@class='checkbox']//label[@for='email_exit']"
    _add_link_type_text_new37 = "//input[@placeholder='Fan Club (default)' and @type='text']"
    _add_button_text_new37 = "//input[@placeholder='Join (default)' and @type='text']"
    _subscription_heading = "subscription_heading"
    _subscription_description = "subscription_description"
    _close_button_text = "close_button_text"
    _fanclubCapturePreview_button = "fanclubCapturePreview"

    # Custom Section
    _add_custom_button = "add_custom_button"
    _add_link_type_text_new38 = "//input[@placeholder='Enter Platform Name']"
    _add_link_url_new38 = "//input[@placeholder='Enter the URL for this track' and @data-type='custom']"

    _custom_dropdown = "//button[@class='btn dropdown-toggle btn-default']//span[text()='PLAY']"
    _select_text = "//ul[@class='dropdown-menu inner']//span[text()='DOWNLOAD']"

    def clickOnTheLink(self):
        self.elementClick(self._login_link, "link")

    def emailSendKeys(self, email):
        self.sendKeys(email, self._email_field)

    def passwordSendKeys(self, password):
        self.sendKeys(password, self._password_field)

    def clickOnTheLoginButton(self):
        self.elementClick(self._login_button)

    def clickShareMusicLink(self):
        self.elementClick(self._share_music_link, "link")

    def clickGateCreateLink(self):
        self.elementClick(self._download_gate_button, "xpath")

    def clickLinkgateLink(self):
        self.elementClick(self._link_gate_button, "xpath")

    def trackUrlSendKeys(self, trackurl):
        self.sendKeys(trackurl, self._track_url)

    def clickOnNextSource(self):
        self.elementClick(self._source_next_button)

    def clickOnGenreCaret(self):
        self.elementClick(self._genre_caret, "xpath")

    def selectGenre(self, ):
        self.elementClick(self._select_genre, "xpath")

    def clickOnNextGenre(self):
        self.elementClick(self._genre_next_button)

    def uploadTrack(self):
        self.sendKeys("C:\\workspace_python\\hypeddit-Project\\Files\\2sec.mp3", self._choose_file)

    def clickOnNextUpload(self):
        self.elementClick(self._upload_next_button)

    def artistNameSendKeys(self, artistname):
        self.sendKeys(artistname, self._artist_name)

    def artistTitleSendKeys(self, artisttitle):
        self.sendKeys(artisttitle, self._track_title)

    def clickOnNextTitle(self):
        self.elementClick(self._title_next_button)

    def uploadImage(self):
        self.elementClick(self._upload_coverart_button)

    def clickDarkScheme(self):
        self.elementClick(self._dark_theme_radio_button, "xpath")

    def clickOnNextDesign(self):
        self.elementClick(self._design_next_button)

    def clickEmCollect(self):
        self.checkRadioElementClick(self._collect_email, "xpath", self._collect_email_id)

    def clickEmCollectName(self):
        self.checkRadioElementClick(self._collect_email_names, "xpath", self._collect_email_names_id)

    def clickEmSkippable(self):
        self.checkRadioElementClick(self._skippable_email, "xpath", self._skippable_email_id)

    def clickScStep(self):
        self.elementClick(self._add_soundcloud_step)

    def clickScFollow(self):
        # self.elementClick(self._follow_profile, "xpath")
        self.checkRadioElementClick(self._follow_profile, "xpath", self._follow_sc_id)

    def clickScComment(self):
        self.checkRadioElementClick(self._comment_sc, "xpath", self._comment_sc_id)

    def clickScLike(self):
        self.checkRadioElementClick(self._like_sc, "xpath", self._like_sc_id)

    def clickScRepost(self):
        self.checkRadioElementClick(self._repost_sc, "xpath", self._repost_sc_id)

    def clickScSkippable(self):
        self.checkRadioElementClick(self._skippable_sc, "xpath", self._skippable_sc_id)

    def profileScSendKeys(self, profile):
        self.sendKeys(profile, self._add_scoundcloud_artist)

    def trackScSendKeys(self, track):
        self.sendKeys(track, self._add_soundcloud_track)

    def clickYtStep(self):
        self.elementClick(self._add_youtube_step)

    def clickYtSubscribe(self):
        self.checkRadioElementClick(self._subscribe_yt, "xpath", self._subscribe_yt_id)

    def clickYtSkippable(self):
        self.checkRadioElementClick(self._skippable_yt, "xpath", self._skippable_yt_id)

    def ytChannelSendKeys(self, url):
        self.sendKeys(url, self._add_channel_yt_url)

    def ytChannelNameSendKeys(self, cName):
        self.sendKeys(cName, self._add_channel_yt_name)

    def clickYtProfileAddButton(self):
        self.elementClick(self._yt_profile_add_button)

    def clickSpStep(self):
        self.elementClick(self._add_spotify_step)

    def clickSpFollow(self):
        self.checkRadioElementClick(self._follow_sp, "xpath", self._follow_sp_id)

    def clickSpSave(self):
        self.checkRadioElementClick(self._save_sp, "xpath", self._save_sp_id)

    def clickSpSkippable(self):
        self.checkRadioElementClick(self._skippable_sp, "xpath", self._skippable_sp_id)

    def spProfileSendKeys(self, profileSp):
        self.sendKeys(profileSp, self._add_artist_sp)

    def spTrackSendKeys(self, trackSp):
        self.sendKeys(trackSp, self._add_track_sp)

    def clickApStep(self):
        self.elementClick(self._add_apple_step)

    def clickApLike(self):
        self.checkRadioElementClick(self._like_ap, "xpath", self._like_ap_id)

    def clickApSave(self):
        self.checkRadioElementClick(self._save_ap, "xpath", self._save_ap_id)

    def clickApSkippable(self):
        self.checkRadioElementClick(self._skippable_ap, "xpath", self._skippable_ap_id)

    def apTrackSendKeys(self, trackUrlAp):
        self.sendKeys(trackUrlAp, self._add_artist_ap)

    def clickDzStep(self):
        self.elementClick(self._add_deezer_step)

    def clickDzFollow(self):
        self.checkRadioElementClick(self._follow_dz, "xpath", self._follow_dz_id)

    def clickDzSave(self):
        self.checkRadioElementClick(self._save_dz, "xpath", self._save_dz_id)

    def clickDzSkippable(self):
        self.checkRadioElementClick(self._skippable_dz, "xpath", self._skippable_dz_id)

    def dzArtistSendKeys(self, artistUrlDz):
        self.sendKeys(artistUrlDz, self._add_artist_dz)

    def dzTrackSendKeys(self, trackUrlDz):
        self.sendKeys(trackUrlDz, self._add_track_dz)

    def clickMcStep(self):
        self.elementClick(self._add_mixcloud_step)

    def clickMcFollow(self):
        self.checkRadioElementClick(self._follow_mc, "xpath", self._follow_mc_id)

    def clickMcRepost(self):
        self.checkRadioElementClick(self._repost_mc, "xpath", self._repost_mc_id)

    def clickMcLike(self):
        self.checkRadioElementClick(self._like_mc, "xpath", self._like_mc_id)

    def clickMcSkippable(self):
        self.checkRadioElementClick(self._skippable_mc, "xpath", self._skippable_mc_id)

    def mcProfileSendKeys(self, profileUrlMc):
        self.sendKeys(profileUrlMc, self._add_artist_mc)

    def mcTrackSendKeys(self, trackUrlMc):
        self.sendKeys(trackUrlMc, self._add_track_mc)

    def clickTwStep(self):
        self.elementClick(self._add_twitter_step)

    def clickTwFollow(self):
        self.checkRadioElementClick(self._follow_tw, "xpath", self._follow_tw_id)

    def clickTwShare(self):
        self.checkRadioElementClick(self._share_tw, "xpath", self._share_tw_id)

    def clickTwSkippable(self):
        self.checkRadioElementClick(self._skippable_tw, "xpath", self._skippable_tw_id)

    def twProfileSendKeys(self, profileUrlTw):
        self.sendKeys(profileUrlTw, self._add_profile_tw)

    def clickThStep(self):
        self.elementClick(self._add_twitch_step)

    def clickThFollow(self):
        self.checkRadioElementClick(self._follow_th, "xpath", self._follow_th_id)

    def clickThSubscription(self):
        self.checkRadioElementClick(self._subscribe_th, "xpath", self._subscribe_th_id)

    def clickThSkippable(self):
        self.checkRadioElementClick(self._skippable_th, "xpath", self._skippable_th_id)

    def thChannelSendKeys(self, channelUrlTh):
        self.sendKeys(channelUrlTh, self._add_artist_th)

    def clickFbMsgrStep(self):
        self.elementClick(self._add_fb_msgr_step)

    def clickFbMsgrSubscription(self):
        self.checkRadioElementClick(self._subscribe_fb_msgr, "xpath", self._subscribe_fb_msgr_id)

    def clickFbMsgrSkippable(self):
        self.checkRadioElementClick(self._skippable_fb_msgr, "xpath", self._skippable_fb_msgr_id)

    def fbMsgrChatbotSendKeys(self):
        self.elementClick(self._chatbot_platform_caret_fb_msgr, "xpath")
        time.sleep(3)
        self.elementClick(self._select_chatbot_fb_msgr, "xpath")

    def fbMsgrPageSendKeys(self, pageUrlFbMsgr):
        self.sendKeys(pageUrlFbMsgr, self._add_page_fb_msgr)

    def clickIgStep(self):
        self.elementClick(self._add_instagram_step)

    def clickIgFollow(self):
        self.checkRadioElementClick(self._follow_ig, "xpath", self._follow_ig_id)

    def clickIgSkippable(self):
        self.checkRadioElementClick(self._skippable_ig, "xpath", self._skippable_ig_id)

    def igProfileSendKeys(self, profileUrlIg):
        self.sendKeys(profileUrlIg, self._add_profile_ig)

    def clickTkStep(self):
        self.elementClick(self._add_tiktok_step)

    def clickTkFollow(self):
        self.checkRadioElementClick(self._follow_tk, "xpath", self._follow_tk_id)

    def clickTkSkippable(self):
        self.checkRadioElementClick(self._skippable_tk, "xpath", self._skippable_tk_id)

    def tkProfileSendKeys(self, profileUrlTk):
        self.sendKeys(profileUrlTk, self._add_profile_tk)

    def clickBcStep(self):
        self.elementClick(self._add_bandcamp_step)

    def clickBcFollow(self):
        self.checkRadioElementClick(self._follow_bc, "xpath", self._follow_bc_id)

    def clickBcSkippable(self):
        self.checkRadioElementClick(self._skippable_bc, "xpath", self._skippable_bc_id)

    def bcProfileSendKeys(self, profileUrlBc):
        self.sendKeys(profileUrlBc, self._add_profile_bc)

    def clickFbStep(self):
        self.elementClick(self._add_facebook_step)

    def clickFbShare(self):
        self.checkRadioElementClick(self._share_fb, "xpath", self._share_fb_id)

    def clickFbLike(self):
        self.checkRadioElementClick(self._like_fb, "xpath", self._like_fb_id)

    def clickFbSkippable(self):
        self.checkRadioElementClick(self._skippable_fb, "xpath", self._skippable_fb_id)

    def fbPageSendKeys(self, pageUrlFb):
        self.sendKeys(pageUrlFb, self._add_page_fb)

    def clickDnStep(self):
        self.elementClick(self._add_donation_step)

    def dnEmailSendKeys(self, emailDn):
        self.sendKeys(emailDn, self._add_donation)

    # -------------------Link Gate----------------

    def artistNameSendkeys(self, artistname):
        self.sendKeys(artistname, self._artist_name)

    def artistTitleSendkeys(self, artistitle):
        self.sendKeys(artistitle, self._link_title)

    def clickTitleNextButton(self):
        self.elementClick(self._title_next_button)

    def secretSendKeys(self, secretLink):
        self.sendKeys(secretLink, self._link_custom_redir_url)

    def clickSecretNextButton(self):
        self.elementClick(self._link_SecretLink_next_button)

    def selectUnlockButtonText(self):
        time.sleep(2)
        self.elementClick(self._link_button_text_dropdown, "xpath")
        time.sleep(2)
        self.elementClick(self._link_menu_select_dropdown, "xpath")

    def clickUnlockNextButton(self):
        self.elementClick(self._link_unlock_button_next_button)

    def designSendKeys(self):
        self.sendKeys("C:\\workspace_python\\hypeddit-Project\\Files\\Tulips.jpg", self._choose_coverart)

    # ------------------Smartlink ---------------------------------------------------
    def clickSmartlinkLink(self):
        self.elementClick(self._smartlink_gate_button, "xpath")

    def clickAudioNextButton(self):
        self.elementClick(self._audio_preview_next_button)

    # Spotify Step

    def clickSaveSp(self):
        self.checkRadioElementClick(self._save_track_spotify, "xpath", self._save_track_spotify_id)

    def clickCaptureEmSp(self):
        self.checkRadioElementClick(self._email_capture_spotify, "xpath", self._email_capture_spotify_id)

    def clickAddPlaylistSp(self):
        self.checkRadioElementClick(self._add_to_playlist_spotify, "xpath", self._add_to_playlist_spotify_id)

    def clickFanProfileSp(self):
        self.checkRadioElementClick(self._follow_spotify_smartlink, "xpath", self._follow_spotify_smartlink_id)

    # Apple step

    def clickSaveAp(self):
        self.checkRadioElementClick(self._save_track_imusic, "xpath", self._save_track_imusic_id)

    def clickAddPlaylistAp(self):
        self.checkRadioElementClick(self._add_to_playlist_imusic, "xpath", self._add_to_playlist_imusic_id)

    def clickLoveTrackAp(self):
        self.checkRadioElementClick(self._follow_imusic, "xpath", self._follow_imusic_id)

    # Deezer Section

    def clickSaveDz(self):
        self.checkRadioElementClick(self._save_track_deezer, "xpath", self._save_track_deezer_id)

    def clickCaptureEmDz(self):
        self.checkRadioElementClick(self._email_capture_deezer, "xpath", self._email_capture_deezer_id)

    def clickAddPlaylistDz(self):
        self.checkRadioElementClick(self._add_to_playlist_deezer, "xpath", self._add_to_playlist_deezer_id)

    def clickFanProfileDz(self):
        self.checkRadioElementClick(self._follow_deezer_smartlink, "xpath", self._follow_deezer_smartlink_id)

    # Hypeddit Section

    def clickHypedditStep(self):
        self.elementClick(self._add_hypeddit_button)

    def hypedditUrlSendKeys(self, Urlhy):
        self.sendKeys(Urlhy, self._add_link_url_new28_hypeddit, "xpath")

    # Email Capture

    def clickEmStep(self):
        self.elementClick(self._add_fanclub_button)

    def clickEmCaptSubscribe(self):
        self.checkRadioElementClick(self._email_link, "xpath", self._email_link_id)

    def emCaptSubscribeExit(self):
        self.checkRadioElementClick(self._email_exit, "xpath", self._email_exit_id)

    def emCaptlinkNameSendKeys(self, linkname):
        self.sendKeys(linkname, self._add_link_type_text_new37, "xpath")

    def emCaptlinkButtonSendKeys(self, linkbutton):
        self.sendKeys(linkbutton, self._add_button_text_new37, "xpath")

    def emCaptHeadLineSendKeys(self, headline):
        self.sendKeys(headline, self._subscription_heading)

    def emCaptParagraphSendKeys(self, paragraph):
        self.sendKeys(paragraph, self._subscription_description)

    def emCaptButtonJoinSendKeys(self, join):
        self.sendKeys(join, self._close_button_text)

    # Share Step

    def clickShareButton(self):
        self.elementClick(self._add_share_button)

    # Custom step

    def clickCustomButton(self):
        self.elementClick(self._add_custom_button)

    def customPlatformSendKeys(self, platform):
        self.sendKeys(platform, self._add_link_type_text_new38, "xpath")

    def customEnterUrlSendKeys(self, trackUrl):
        self.sendKeys(trackUrl, self._add_link_url_new38, "xpath")

    def clickButtonText(self):
        self.elementClick(self._custom_dropdown, "xpath")

    def clickSelectText(self):
        self.elementClick(self._select_text, "xpath")

    # ------------------------------xxx-------------------------------

    def clickOnNextGateSteps(self):
        self.elementClick(self._gate_step_next_button)

    def editCustomLink(self):
        self.elementClick(self._edit_custom_link)

    def pageSendKeys(self, pagename):
        self.sendKeys(pagename, self._page)

    def optionalSendKeys(self, optional):
        self.sendKeys(optional, self._optional)

    def clickOnNextLinkUrl(self):
        self.elementClick(self._linkUrl_next_button)

    def clickPublic(self):
        self.elementClick(self._set_newRelease_public, "xpath")

    def clickNewRelease(self):
        self.elementClick(self._set_newRelease, "xpath")

    def clickOnNextReleaseSettings(self):
        self.elementClick(self._release_settings_button)

    def clickOnEmailPromotionCaret(self):
        self.elementClick(self._email_promotion_caret, "xpath")

    def selectFangate(self):
        self.elementClick(self._select_fangate, "xpath")

    def clickOnNextEmailPromotion(self):
        self.elementClick(self._email_promotion_next_button)

    def facebookPixelSendKeys(self, fbpixel):
        self.sendKeys(fbpixel, self._facebook_pixel)

    def facebookTokenSendKeys(self, fbtoken):
        self.sendKeys(fbtoken, self._facebook_pixel_token)

    def clickOnNextTrackingPixels(self):
        self.elementClick(self._tracking_pixels_next_button)

    def clickOnCreate(self):
        self.elementClick(self._create_fangate_button)

    def clickOnCreatLinkGate(self):
        self.elementClick(self._create_linkgate_button)

    def waitFor(self):
        self.waitForElement(self._dark_theme_radio_button)

    def devUnlockPasswordSendkeys(self, passwordtext):
        self.sendKeys(passwordtext, self._dev_unlock_password, "xpath")

    def devUnlockbuttonClick(self):
        self.elementClick(self._dev_unlock_button, "xpath")

    def waitFl(self,loc,lid="id"):
        self.waitForElement(loc,lid,20,.5)


    def createFangate(self, Fg, artistname="sunil", trackurl="https://soundcloud.com/makelogin/sleep-away",
                      artisttitle="verma", fbpixel=7, fbtoken=8):
        if Fg == "fangate":
            time.sleep(2)
            self.waitFl(self._share_music_link, "link")
            self.clickShareMusicLink()
            time.sleep(1)
            self.clickGateCreateLink()

            self.source(trackurl, Fg)
            self.genre()
            time.sleep(2)
            self.upload()
            time.sleep(2)
            self.title(artistname, artisttitle)
            time.sleep(2)
            self.design()
        if Fg == "linkgate":
            time.sleep(2)
            self.waitFl(self._share_music_link, "link")
            self.clickShareMusicLink()
            time.sleep(1)
            self.clickLinkgateLink()

            self.linkTitle()
            self.linkSecret()
            self.linkUnlock()
            self.linkDesignStep()

        if Fg == "smartlink":
            time.sleep(2)
            self.waitFl(self._share_music_link, "link")
            self.clickShareMusicLink()
            time.sleep(1)
            self.clickSmartlinkLink()
            self.source("USNRS1229743", Fg)
            self.genre()
            time.sleep(2)
            # self.upload()
            # time.sleep(2)
            self.title(artistname, artisttitle)
            time.sleep(2)
            self.design()

        if Fg == "fangate":
            self.gateSteps(Fg)
        elif Fg == "linkgate":
            self.gateSteps(Fg)
        elif Fg == "smartlink":
            self.linkSteps()


        time.sleep(2)
        self.linkUrl()
        time.sleep(2)
        self.releaseSettings(Fg)
        time.sleep(2)

        if Fg == "fangate":
            self.emailPromotion()
        elif Fg == "linkgate":
            self.emailPromotion()
        elif Fg == "smartlink":
            self.audioPreview()
            time.sleep(2)

        self.trackingPixels(fbpixel, fbtoken)
        time.sleep(2)
        self.confirmation(Fg)
        time.sleep(2)

    def clearFields(self):
        element = self.getElement(self._email_field)
        element.clear()

        element = self.getElement(self._password_field)
        element.clear()

    def devUnlock(self, unlockpassword="testdev123"):
        self.devUnlockPasswordSendkeys(unlockpassword)
        self.devUnlockbuttonClick()

    def source(self, trackurl, Fg):
        self.trackUrlSendKeys(trackurl)
        time.sleep(1)
        self.clickOnNextSource()
        self.waitFl(self._genre_caret, "xpath")


        #if Fg == "smartlink":
            #time.sleep(20)
        #else:
            #time.sleep(2)

    def genre(self):
        #time.sleep(5)
        self.clickOnGenreCaret()
        self.waitFl(self._select_genre,"xpath")
        self.selectGenre()
        self.waitFl(self._genre_next_button)
        self.clickOnNextGenre()

    def upload(self):
        self.uploadTrack()
        time.sleep(3)
        self.clickOnNextUpload()

    def title(self, artistname, artisttitle):
        self.artistNameSendKeys(artistname)
        time.sleep(1)
        self.artistTitleSendKeys(artisttitle)
        time.sleep(1)
        self.clickOnNextTitle()

    def design(self):
        # Skip Coverart
        # self.waitFor()
        self.clickDarkScheme()
        time.sleep(1)
        self.clickOnNextDesign()

    _ad_soundcloud_artist = "add_soundcloud_artist"
    _ad_soundcloud_loader = "//div[@id='add_soundcloud_loader'][contains(@class,'select-loading hide')]"
    _sc_select_profile_1 = "//li[@data-userid='173804369']"

    def scArtistSendKeys(self, artistname):
        self.waitFl(self._ad_soundcloud_artist)
        self.sendKeys(artistname, self._ad_soundcloud_artist)

    def checkLoaderElement(self, loc, ltype="id"):
        return self.isElementPresent(loc, ltype)

    def clickScArtist(self):
        self.elementClick(self._sc_select_profile_1, "xpath")


    def selectArtistSc(self):
        self.scArtistSendKeys("lata")
        for i in range(51):
            if i > 49:
                break
            time.sleep(2)
            if self.checkLoaderElement(self._ad_soundcloud_loader, "xpath") == True:
                self.clickScArtist()
                break

    _add_spotify_artist = "add_spotify_artist"
    _add_spotify_loader = "//div[@id='add_spotify_loader'][contains(@class,'select-loading hide')]"
    _sp_select_profile_1 = "//li[@data-userid='1D8jzmybTOgH82MsFsCxKf']"

    def spArtistSendKeys(self, artistname):
        self.waitFl(self._ad_soundcloud_artist)
        self.sendKeys(artistname, self._add_spotify_artist)

    # def checkLoaderElement(self, loc, ltype="id"):
    #     return self.isElementPresent(loc, ltype)

    def clickSpArtist(self):
        self.elementClick(self._sp_select_profile_1, "xpath")

    def selectArtistSp(self):
        self.spArtistSendKeys("lata")
        for i in range(51):
            if i > 49:
                break
            time.sleep(2)
            if self.checkLoaderElement(self._add_spotify_loader, "xpath") == True:
                self.clickSpArtist()
                break

    _add_deezer_artist = "add_deezer_artist"
    _add_deezer_loader = "//div[@id='add_deezer_loader'][contains(@class,'select-loading hide')]"
    _dz_select_profile_1 = "//li[@data-userid='310646845']"

    def dzArtistSendKeys(self, artistname):
        self.waitFl(self._add_deezer_artist)
        self.sendKeys(artistname, self._add_deezer_artist)

    # def checkLoaderElement(self, loc, ltype="id"):
    #     return self.isElementPresent(loc, ltype)

    def clickDzArtist(self):
        self.elementClick(self._dz_select_profile_1, "xpath")

    def selectArtistDz(self):
        self.dzArtistSendKeys("lata")
        for i in range(51):
            if i > 49:
                break
            time.sleep(2)
            if self.checkLoaderElement(self._add_deezer_loader, "xpath") == True:
                self.clickDzArtist()
                break

    _add_mixcloud_artist = "add_mixcloud_artist"
    _add_mixcloud_loader = "//div[@id='add_mixcloud_loader'][contains(@class,'select-loading hide')]"
    _mx_select_profile_1 = "//li[@data-userid='latae-korakoth']"

    def mxArtistSendKeys(self, artistname):
        self.waitFl(self._add_mixcloud_artist)
        self.sendKeys(artistname, self._add_mixcloud_artist)

    # def checkLoaderElement(self, loc, ltype="id"):
    #     return self.isElementPresent(loc, ltype)

    def clickMxArtist(self):
        self.elementClick(self._mx_select_profile_1, "xpath")

    def selectArtistMx(self):
        self.mxArtistSendKeys("lata")
        for i in range(51):
            if i > 49:
                break
            time.sleep(2)
            if self.checkLoaderElement(self._add_mixcloud_loader, "xpath") == True:
                self.clickMxArtist()
                break

    _add_facebook = "add_facebook"
    #_add_mixcloud_loader = "//div[@id='add_mixcloud_loader'][contains(@class,'select-loading hide')]"
    _fb_select_profile_1 = "//ul[@id='facebook_artist_search']//li[@data-userid='904258603054194']"

    def fbArtistSendKeys(self, artistname):
        self.waitFl(self._add_facebook)
        self.sendKeys(artistname, self._add_facebook)

    # def checkLoaderElement(self, loc, ltype="id"):
    #     return self.isElementPresent(loc, ltype)

    def clickFbArtist(self):
        self.elementClick(self._fb_select_profile_1, "xpath")

    def selectArtistFb(self):
        self.fbArtistSendKeys("Sonu")
        self.waitFl(self._fb_select_profile_1, "xpath")
        self.clickFbArtist()

    _soundcloud_profile_add_button = "soundcloud_profile_add_button"

    def scProfileClickButton(self):
        self.waitFl(self._soundcloud_profile_add_button)
        self.elementClick(self._soundcloud_profile_add_button)

    def gateSteps(self, Fg):
        # ----------------Email Step------------------------------
        time.sleep(3)
        self.clickEmCollect()
        self.clickEmCollectName()
        self.clickEmSkippable()
        # -------------------Soundlcoud Step---------------------------
        if Fg == "linkgate":
            self.clickScStep()

        time.sleep(3)
        self.clickScFollow()
        self.clickScComment()
        self.clickScLike()
        self.clickScRepost()
        self.clickScSkippable()
        if Fg == "linkgate":
            #self.profileScSendKeys("https://soundcloud.com/makelogin")
            self.selectArtistSc()
            self.trackScSendKeys("https://soundcloud.com/makelogin/sleep-away")

        if Fg == "fangate":
            #self.profileScSendKeys("https://soundcloud.com/makelogin")
            self.scProfileClickButton()
            self.selectArtistSc()
            #self.trackScSendKeys("https://soundcloud.com/makelogin/sleep-away")


        # Skip Profile SC
        # Skip Title SC

        # --------------------Youtube Step---------------------------
        time.sleep(3)
        self.clickYtStep()
        time.sleep(3)
        self.clickYtSubscribe()
        self.clickYtSkippable()
        self.ytChannelSendKeys("https://www.youtube.com/user/DoctoresseBonneto")
        self.ytChannelNameSendKeys("Cname")
        self.clickYtProfileAddButton()

        # ---------------------Apple Step------------------------------
        time.sleep(3)
        self.clickApStep()
        time.sleep(2)
        self.clickApStep()
        self.clickApLike()
        self.clickApSave()
        self.clickApSkippable()
        self.apTrackSendKeys("https://music.apple.com/in/album/humdard/1111741333?i=1111741446")

        # -------------------------------Spotify Step --------------------------

        time.sleep(3)
        self.clickSpStep()

        self.clickSpFollow()
        self.clickSpSave()
        self.clickSpSkippable()
        self.selectArtistSp()
        #self.spProfileSendKeys("https://open.spotify.com/artist/11bBHpkCZPkktTsrXAZyql")
        self.spTrackSendKeys("https://open.spotify.com/track/0VbRRS6pOgCvepxNiAz2fY")

        # ---------------------Deezer Step------------------------------
        time.sleep(3)
        self.clickDzStep()
        self.clickDzFollow()
        self.clickDzSave()
        self.clickDzSkippable()
        self.selectArtistDz()
        #self.dzArtistSendKeys("https://www.deezer.com/us/artist/661247")
        self.dzTrackSendKeys("https://www.deezer.com/us/track/15211178")

        # ---------------------Mixcloud Step------------------------------
        time.sleep(3)
        self.clickMcStep()
        self.clickMcFollow()
        self.clickMcRepost()
        self.clickMcLike()
        self.clickMcSkippable()
        self.selectArtistMx()
        #self.mcProfileSendKeys("https://www.mixcloud.com/gabrydemartini")
        self.mcTrackSendKeys("https://www.mixcloud.com/felixdahousecat/chicago-blakkout-episode-14/")

        # ---------------------Twitter Step------------------------------
        time.sleep(3)
        self.clickTwStep()
        self.clickTwFollow()
        self.clickTwShare()
        self.clickTwSkippable()
        self.twProfileSendKeys("https://twitter.com/csswg")

        # ---------------------Twitch Step------------------------------
        time.sleep(3)
        self.clickThStep()
        self.clickThFollow()
        self.clickThSubscription()
        self.clickThSkippable()
        self.thChannelSendKeys("sweet_anita")

        # ---------------------Messenger Step------------------------------
        time.sleep(3)
        self.clickFbMsgrStep()
        self.clickFbMsgrSubscription()
        self.clickFbMsgrSkippable()
        time.sleep(2)
        self.fbMsgrChatbotSendKeys()
        self.fbMsgrPageSendKeys('https://www.facebook.com/Test-company-109379167072055')

        # ---------------------Instagram Step------------------------------
        time.sleep(3)
        self.clickIgStep()
        self.clickIgFollow()
        self.clickIgSkippable()
        self.igProfileSendKeys("https://www.instagram.com/hypeddit")

        # ---------------------TikTok Step------------------------------
        time.sleep(3)
        self.clickTkStep()
        self.clickTkFollow()
        self.clickTkSkippable()
        self.tkProfileSendKeys("https://www.tiktok.com/hypeddit")

        # ---------------------Bandcamp Step------------------------------
        time.sleep(3)
        self.clickBcStep()
        self.clickBcFollow()
        self.clickBcSkippable()
        self.bcProfileSendKeys("https://www.bandcamp.com/hypeddit")

        # ---------------------Facebook Step------------------------------
        time.sleep(3)
        self.clickFbStep()
        self.clickFbShare()
        self.clickFbLike()
        self.clickFbSkippable()
        self.selectArtistFb()
        #self.fbPageSendKeys("https://www.facebook.com/hypeddit")

        # ---------------------Donation Step------------------------------
        time.sleep(3)
        self.clickDnStep()
        self.dnEmailSendKeys("testing001web@gmail.com")

        self.clickOnNextGateSteps()
        time.sleep(1)
        self.clickOnNextGateSteps()

    def linkUrl(self):
        # Skip Edit Custom Url
        # skip page text Edit
        # skip optional Edit
        self.waitFl(self._linkUrl_next_button)
        self.clickOnNextLinkUrl()


    def releaseSettings(self, Fg):
        if Fg == "fangate":
            # self.clickPublic()
            time.sleep(1)
            self.clickNewRelease()
        elif Fg == "smartlink":
            time.sleep(1)
            self.clickNewRelease()

        time.sleep(1)
        self.clickOnNextReleaseSettings()

    def emailPromotion(self):
        self.clickOnEmailPromotionCaret()
        time.sleep(1)
        self.selectFangate()
        time.sleep(1)
        self.clickOnNextEmailPromotion()

    def trackingPixels(self, fbpixel, fbtoken):
        self.facebookPixelSendKeys(fbpixel)
        time.sleep(1)
        self.facebookTokenSendKeys(fbtoken)
        time.sleep(15)
        self.clickOnNextTrackingPixels()

    def confirmation(self, Fg):
        if Fg == "fangate":
            self.clickOnCreate()
        elif Fg == "smartlink":
            self.clickOnCreate()
            time.sleep(60)
        else:
            self.clickOnCreatLinkGate()

    def linkTitle(self):
        time.sleep(1)
        self.artistNameSendkeys("anil")
        time.sleep(1)
        self.artistTitleSendkeys("sharma")
        time.sleep(1)
        self.clickTitleNextButton()

    def linkSecret(self):
        time.sleep(1)
        self.secretSendKeys("https://www.google.com")
        time.sleep(1)
        self.clickSecretNextButton()

    def linkUnlock(self):
        time.sleep(1)
        self.selectUnlockButtonText()
        time.sleep(1)
        self.clickUnlockNextButton()

    def linkDesignStep(self):
        time.sleep(1)
        self.designSendKeys()
        time.sleep(5)
        self.clickDarkScheme()
        time.sleep(1)
        time.sleep(1)
        self.clickOnNextDesign()
        time.sleep(1)

    def audioPreview(self):
        self.clickAudioNextButton()

    def linkSteps(self):
        # Spotify step
        time.sleep(1)
        self.clickSaveSp()
        self.clickCaptureEmSp()
        self.clickAddPlaylistSp()
        self.clickFanProfileSp()
        self.spProfileSendKeys("https://open.spotify.com/artist/11bBHpkCZPkktTsrXAZyql")

        # Apple Step
        time.sleep(1)
        self.clickApSave()
        self.clickAddPlaylistAp()
        self.clickLoveTrackAp()

        # Deezer Step
        time.sleep(1)
        self.clickSaveDz()
        self.clickCaptureEmDz()
        self.clickAddPlaylistDz()
        self.clickFanProfileDz()
        self.dzArtistSendKeys("https://www.deezer.com/us/artist/661247")

        # Hypeddit Step
        time.sleep(1)
        self.clickHypedditStep()
        time.sleep(1)
        self.hypedditUrlSendKeys("https://hypeddit.com/track/vz2rfn")

        # Email Capture Step
        self.clickEmStep()
        self.clickEmCaptSubscribe()
        self.emCaptSubscribeExit()
        self.emCaptlinkNameSendKeys("my name")
        self.emCaptlinkButtonSendKeys("link Button")
        self.emCaptHeadLineSendKeys("Sub Heading")
        self.emCaptParagraphSendKeys("Paragraph")
        self.emCaptButtonJoinSendKeys("Buttton Join")

        # Share Button Step

        self.clickShareButton()

        # Custom Section

        self.clickCustomButton()
        self.customPlatformSendKeys("test platform")
        self.customEnterUrlSendKeys("https://www.soundcloud.com")
        time.sleep(1)
        self.clickButtonText()
        time.sleep(1)
        self.clickSelectText()

        self.clickOnNextGateSteps()


        # https://216.172.171.124:2083
        #
        # nupasta.com
        #
        # U: nupastcom
        # P: wlZQ^se7#$9Ls.amP
        #
        #
        # CMSadmin
        #
        #
        #
        # HH)25tz9j!F%^mF9!DBoJH$*
