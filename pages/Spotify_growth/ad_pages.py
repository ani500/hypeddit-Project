import time
import threading
import pytest

from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as c1
import logging
import time


class AdPage(SeleniumDriver):
    log = c1.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    # Locators
    _promote_music = "//a[@href='https://dev2.hypeddit.com/promotemusic']"
    _ad_templates = "//a[@href='https://dev2.hypeddit.com/ads/templates']"
    _spotify_growth_track = "//a[@href='https://dev2.hypeddit.com/ads/create/spotify-growth-track']"
    _spotify_growth_playlist = "//a[@href='https://dev2.hypeddit.com/ads/create/spotify-growth-playlist']"
    _spotify_growth_artist = "//a[@href='https://dev2.hypeddit.com/ads/create/spotify-growth-artist']"
    _spotify_growth_email = "//a[@href='https://dev2.hypeddit.com/ads/create/grow-my-fan-emails']"

    _goal_next_button = "next_box_button_choose-type"

    _page_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Select page']"
    _select_page = "//ul[@class='dropdown-menu inner']//span[text()='Musical']"
    _fbaccount_caret = "//button[@data-id='ads_account_id']//span[text()='Select account']"
    _select_fbaccount = "//ul[@class='dropdown-menu inner']//span[text()='myaddaccount [439792928095444]']"
    _igaccount_caret = "//button[@data-id='instagram_account_id']//span[text()='Select account']"
    _select_igaccount = "//ul[@class='dropdown-menu inner']//span[text()='phoolpareta']"
    _pixelaccount_caret = "//button[@data-id='facebook_pixel_id']//span[text()='Select pixel']"
    _select_pixelaccount = "//ul[@class='dropdown-menu inner']//span[text()='second pixel [1242408256319578]']"

    _accounts_next_button = "next_box_button_facebook-account-connect"

    _spotify_url = "track_url"
    _spotify_playlist_url = "playlist_url"
    _spotify_artist_url = "artist_url"
    _artist_name = "artist_name"
    _artist_title = "title"
    _genre_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Select genre']"
    _select_genre = "//ul[@class='dropdown-menu inner']//span[text()='Bass']"
    _giveaway_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Select a fan giveaway']"
    _select_giveaway = "//span[text()='Sample Pack Download']"
    _music_next_button = "next_box_button_music"
    _choose_file = "inputFileAudioAsset"

    _ad_inputManualCoverart = "inputManualCoverart"
    _ad_inputFileAudioAsset = "inputFileAudioAsset"
    _ad_inputFilemp4 = "inputFilemp4"
    _ad_next_button = "next_box_button_audio-video"
    _ad_inputFileAudioUpload = "inputFileAudioUpload"

    _countries_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Tier One Countries ']"
    _select_countries = "//ul[@class='dropdown-menu inner']//span[text()='All Countries']"
    _countries_next_button = "next_box_button_countries"

    _ad_spotify_artists = "add_spotify_artist"
    _interest_button = "generateInterestsButton"
    _interest_next_button = 'next_box_button_interests'

    _budget_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Choose INR Per Day']"
    _select_budget = "//ul[@class='dropdown-menu inner']//span[text()='420']"
    _budget_next_button = "next_box_button_budget"

    _advance_min_age_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='18']"
    _select_min_age = "//div[@class='btn-group bootstrap-select form-control dropup open']//span[text()='19']"
    _advance_max_age_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='65+']"
    _select_max_age = "//div[@class='btn-group bootstrap-select form-control dropup open']//span[text()='61']"

    _advance_gender_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='All']"
    _select_gender = "//ul[@class='dropdown-menu inner']//span[text()='Men']"
    _head_link_override = "headline_top_text_override"
    _advance_next_button = "next_box_button_advanced"

    _common_terms = "//div[@class='checkbox']//label[@for='common_terms']"
    _common_terms_id = "common_terms"
    _facebook_terms = "//div[@class='checkbox']//label[@for='facebook_terms']"
    _facebook_terms_id = "facebook_terms"
    _hypeddit_terms = "//div[@class='checkbox']//label[@for='hypeddit_terms']"
    _hypeddit_terms_id = "hypeddit_terms"
    _save_draft_button = "next_box_button_confirmation"

    _loader_image = "//img[@title='45 sec']"
    _music_loader_image = "//div[@class='loader select-loading'][contains(@style,'display: block')]"

    _interest_loader_image = "//div[@id='related_artists_interest_main'][contains(@class,'hide')]"
    _interest_loader_profile = "//div[@id='add_spotify_loader'][contains(@class,'select-loading hide')]"
    _interest_generate_profile = "//div[@id='spotify_search_div_loading'][contains(@class,'hide')]"

    _artist_name_music_reward = "artist_name"
    _artist_name_loader_reward = "//div[@id='artist_name_loader'][contains(@class,'select-loading hide')]"

    _interest_select_profile_1 = "//li[@data-userid='61JrslREXq98hurYL2hYoc']"
    _interest_select_profile_2 = "//li[@data-userid='5OHhhP4Nxp1z0BCHYCkDAK']"
    _interest_select_profile_3 = "//li[@data-userid='5as8A4G47Ohu9NSWs3Je8U']"

    # facebook Window Locators
    _facebook_button = "AdsFacebookLogin"
    _facebook_confirm_button = "//span[text()='Continue as Anil Sharma']"
    _facebook_email = "email"
    _facebook_pass = "pass"
    _facebook_login_button = "//input[@value='Log in']"
    # budget locators
    _schedule_radio_button = "//div[@class='checkbox']//label[@for='ad_scheduled']"
    _time_zone_caret = "//button[@class='btn dropdown-toggle btn-default']//span[text()='Alaska (GMT-09:00)']"
    _select_zone = "//div[@class='btn-group bootstrap-select form-control dropup open']//span[text()='Arizona (GMT-07:00)']"

    #  Calender Locators
    _music_calendar = "release_datetime"
    _date_select_music ="//div[contains(@class,'xdsoft_datetimepicker xdsoft_ xdsoft_noselect ') and contains(@style,'display: block')]//following-sibling::tr[4]//following-sibling::td[6]"

    # Music Rewards
    _title_music_reward = "title"
    def clickPromoteLink(self):
        self.elementClick(self._promote_music, "xpath")

    def clickAdTemplateButton(self):
        self.elementClick(self._ad_templates, "xpath")

    def clickSpotifyGrowthTrack(self):
        self.elementClick(self._spotify_growth_track, "xpath")

    def clickSpotifyGrowthPlaylist(self):
        self.elementClick(self._spotify_growth_playlist, "xpath")

    def clickSpotifyGrowthArtist(self):
        self.elementClick(self._spotify_growth_artist, "xpath")

    def clickSpotifyGrowthEmail(self):
        self.elementClick(self._spotify_growth_email, "xpath")

    def clickGoalNextButton(self):
        self.elementClick(self._goal_next_button)

    def clickOnFbPage(self):
        self.elementClick(self._page_caret, "xpath")

    def selectFbPage(self):
        self.elementClick(self._select_page, "xpath")

    def clickOnFbPageAccount(self):
        self.elementClick(self._fbaccount_caret, "xpath")

    def selectFbPageAccount(self):
        self.elementClick(self._select_fbaccount, "xpath")

    def clickOnIgPageAccount(self):
        self.elementClick(self._igaccount_caret, "xpath")

    def selectIgPageAccount(self):
        self.elementClick(self._select_igaccount, "xpath")
        self.elementClick(self._select_igaccount, "xpath")

    def clickOnPixelAccount(self):
        self.elementClick(self._pixelaccount_caret, "xpath")

    def selectPixelAccount(self):
        self.elementClick(self._select_pixelaccount, "xpath")

    def clickAccountNextButton(self):
        self.elementClick(self._accounts_next_button)

    def spUrlSendKeys(self, spUrl):
        self.waitFl(self._spotify_url)
        self.sendKeys(spUrl, self._spotify_url)

    def clickMusicDateField(self):
        self.waitFl(self._music_calendar)
        self.elementClick(self._music_calendar)

    def selectMusicDate(self):
        self.waitFl(self._date_select_music, 'xpath')
        self.elementClick(self._date_select_music,'xpath')

    def spPlaylistUrlSendKeys(self, spUrl):
        self.sendKeys(spUrl, self._spotify_playlist_url)

    def spArtistUrlSendKeys(self, spUrl):
        self.sendKeys(spUrl, self._spotify_artist_url)

    def artistSendKeys(self, artistName):
        self.sendKeys(artistName, self._artist_name)

    def titleSendKeys(self, artistTitle):
        self.sendKeys(artistTitle, self._artist_title)

    def clickArtistField(self):
        self.elementClick(self._artist_name)

    def clickOnGenre(self):
        self.elementClick(self._genre_caret, "xpath")

    def selectGenre(self):
        self.elementClick(self._select_genre, "xpath")

    def uploadTrackArtist(self):
        self.sendKeys("D:\\workspace_python\\hypeddit-Project\\Files\\2sec.mp3", self._choose_file)

    def clickGiveaway(self):
        self.elementClick(self._giveaway_caret, "xpath")

    def selectGiveaway(self):
        self.elementClick(self._select_giveaway, "xpath")

    def clickMusicNextButton(self):
        self.elementClick(self._music_next_button)

    def mp3SendKeys(self, filePathmp3):
        self.sendKeys(filePathmp3, self._ad_inputFileAudioAsset)

    def mp3SendKeysReward(self, filePathmp4):
        self.sendKeys(filePathmp4, self._ad_inputFileAudioUpload)

    def mp4SendKeys(self, filePathmp4):
        self.sendKeys(filePathmp4, self._ad_inputFilemp4)

    def clickAdNextButton(self):
        self.elementClick(self._ad_next_button)

    def clickOnCountryList(self):
        self.elementClick(self._countries_caret, "xpath")

    def selectCountries(self):
        self.elementClick(self._select_countries, "xpath")

    def clickCountriesNextButton(self):
        self.elementClick(self._countries_next_button)

    def spArtistSendKeys(self, artistName):
        self.sendKeys(artistName, self._ad_spotify_artists)

    def spArtistSendKeysMusicReward(self, artistName):
        self.waitFl(self._artist_name_music_reward)
        self.sendKeys(artistName, self._artist_name_music_reward)

    def clickGenerateInterestButton(self):
        self.elementClick(self._interest_button)

    def clickInterestNextButton(self):
        self.elementClick(self._interest_next_button)

    def clickInterestArtist1(self):
        self.elementClick(self._interest_select_profile_1, "xpath")

    def clickInterestArtist2(self):
        self.elementClick(self._interest_select_profile_2, "xpath")

    def clickInterestArtist3(self):
        self.elementClick(self._interest_select_profile_3, "xpath")

    def clickOnBudget(self):
        self.elementClick(self._budget_caret, "xpath")

    def selectBudgetAmount(self):
        self.elementClick(self._select_budget, "xpath")

    def clickBudgetNextButton(self):
        self.elementClick(self._budget_next_button)

    def clickOnSelectMinAge(self):
        self.elementClick(self._advance_min_age_caret, "xpath")

    def selectMinAge(self):
        self.elementClick(self._select_min_age, "xpath")

    def clickOnSelectMaxAge(self):
        self.elementClick(self._advance_max_age_caret, "xpath")

    def selectMaxAge(self):
        self.elementClick(self._select_max_age, "xpath")

    def clickOnSelectGender(self):
        self.elementClick(self._advance_gender_caret, "xpath")

    def selectGender(self):
        self.elementClick(self._select_gender, "xpath")

    def overRideTextSendKeys(self, overridetext):
        self.sendKeys(overridetext, self._head_link_override)

    def clickAdvancetNextButton(self):
        self.elementClick(self._advance_next_button)

    def clickCommonTerms(self):
        self.checkRadioElementClick(self._common_terms, "xpath", self._common_terms_id)

    def clickFbTerms(self):
        self.checkRadioElementClick(self._facebook_terms, "xpath", self._facebook_terms_id)

    def clickHypedditTerms(self):
        self.checkRadioElementClick(self._hypeddit_terms, "xpath", self._hypeddit_terms_id)

    def clickDraftNextButton(self):
        self.elementClick(self._save_draft_button)

    def waitFl(self, loc, lid="id"):
        self.waitForElement(loc, lid, 50, .5)

    def checkLoaderElement(self, loc, ltype="id"):
        return self.isElementPresent(loc, ltype)

    # facebook window

    def clickFbConnectButton(self):
        self.elementClick(self._facebook_button)

    def fbEmailSendKeys(self, fbEmail):
        self.sendKeys(fbEmail, self._facebook_email)

    def fbPassSendKeys(self, fbEmail):
        self.sendKeys(fbEmail, self._facebook_pass)

    def sendKeysTitleMusic(self, title):
        self.waitFl(self._title_music_reward)
        self.sendKeys(title, self._title_music_reward)

    def clickFbLoginButton(self):
        self.elementClick(self._facebook_login_button, "xpath")

    def clickFbConfirmButton(self):
        self.elementClick(self._facebook_confirm_button, "xpath")

    def createAd(self, AdType):
        # self.driver.get("https://dev2.hypeddit.com/ads/create/spotify_growth_track")
        self.waitFl(self._promote_music, "xpath")
        self.clickPromoteLink()
        self.waitFl(self._ad_templates, "xpath")
        self.clickAdTemplateButton()
        self.waitFl(self._spotify_growth_track, "xpath")

        if AdType == 'track':
            self.clickSpotifyGrowthTrack()

        if AdType == 'playlist':
            self.clickSpotifyGrowthPlaylist()

        if AdType == 'artist':
            self.clickSpotifyGrowthArtist()

        if AdType == 'fanemail':
            self.clickSpotifyGrowthEmail()

        if AdType == 'presave_reward':
            self.driver.get("https://dev2.hypeddit.com/ads/create/spotify-growth-presave-reward")

        self.accountprofile()
        #self.clickAccountNextButton()
        self.music(AdType)
        self.ad()

        self.countries()
        # self.waitFl(self._interest_button)
        self.interest()

        self.budget()

        self.advance()
        self.confirmation()
        time.sleep(50)

    def goal(self):
        self.clickGoalNextButton()

    def accountprofile(self):

        self.clickFbConnectButton()
        time.sleep(2)
        self.switchWindowHander(0)
        time.sleep(2)
        self.fbEmailSendKeys("anilangira@gmail.com")
        time.sleep(2)
        self.fbPassSendKeys("KUL@o5678")
        time.sleep(2)
        self.clickFbLoginButton()
        self.waitFl(self._facebook_confirm_button, "xpath")
        self.clickFbConfirmButton()
        time.sleep(2)
        # self.driver.close()
        self.switchWindowHander(1)

        self.waitFl(self._page_caret, "xpath")
        time.sleep(2)
        self.clickOnFbPage()
        time.sleep(2)
        self.selectFbPage()
        time.sleep(2)
        self.waitFl(self._fbaccount_caret, "xpath")
        self.clickOnFbPageAccount()
        time.sleep(2)
        self.selectFbPageAccount()
        # self.waitFl(self._igaccount_caret, "xpath")
        # self.clickOnIgPageAccount()
        # self.selectIgPageAccount()
        self.waitFl(self._pixelaccount_caret, "xpath")
        self.clickOnPixelAccount()
        time.sleep(2)
        self.selectPixelAccount()
        self.clickAccountNextButton()

    def music(self, AdType):

        if AdType == 'track':
            self.spUrlSendKeys("USNRS1229743")
            # self.clickArtistField()

        if AdType == 'playlist':
            self.spPlaylistUrlSendKeys("https://open.spotify.com/playlist/3zCIdLCGKOFa3XWq1yo5SF?si=9d51f2ecd9d14327")

        if AdType == 'artist':
            self.spArtistUrlSendKeys("https://open.spotify.com/artist/4YRxDV8wJFPHPTeXepOstw?si=uRUhhlyQS1mYyzrXaHtHSg")

        if AdType == 'fanemail':
            self.waitFl(self._giveaway_caret, 'xpath')
            self.clickGiveaway()
            self.waitFl(self._select_giveaway, 'xpath')
            self.selectGiveaway()
            self.spUrlSendKeys(
                "https://soundcloud.com/purifiedrec/serra-9-deviu-feat-phoebe-tsen?in_system_playlist=personalized-tracks%3A%3Atesting-user-724105926%3A1344956383")

        if AdType == 'presave_reward':

            self.spUrlSendKeys("USNRS1229743")
            self.clickMusicDateField()
            self.selectMusicDate()
            self.spArtistSendKeysMusicReward("lata")
            for i in range(51):
                if i > 49:
                    break
                time.sleep(2)
                if self.checkLoaderElement(self._artist_name_loader_reward, "xpath") == True:
                    self.clickInterestArtist1()
                    break

            self.sendKeysTitleMusic("testtitle")



        if AdType=="track" and AdType=="playlist" and AdType=="artist":



            for i in range(200):
                if i > 198:
                    break
                time.sleep(2)
                if self.checkLoaderElement(self._music_loader_image, "xpath") == False:

                    if AdType == 'playlist':
                        self.spUrlSendKeys("https://open.spotify.com/track/7gFu2zjthH2zPbyl4uHLpr?si=e7a5fd99fcb54256")
                        time.sleep(5)  # waiting for the loader to complete
                break

        self.waitFl(self._genre_caret, "xpath")
        self.clickOnGenre()
        self.selectGenre()

        if AdType == "presave_reward":
            time.sleep(10)
            self.mp3SendKeysReward("D:\\workspace_python\\hypeddit-Project\\Files\\45 sec.mp3")
        if AdType == 'fanemail':
            self.waitFl(self._choose_file)
            self.uploadTrackArtist()
        time.sleep(10)
        self.clickMusicNextButton()






    def ad(self):
        time.sleep(15)
        self.mp3SendKeys("D:\\workspace_python\\hypeddit-Project\\Files\\45 sec.mp3")
        # self.mp4SendKeys("C:\\Users\\Anil\\workspace_python\\hypeddit-Project\\Files\\Hazard Lights - SGE Cover - Preview 1.mp4")
        time.sleep(4)
        for i in range(500):
            if i > 100:
                break
            time.sleep(2)
            if self.checkLoaderElement(self._loader_image, "xpath") == False:
                self.clickAdNextButton()
                print("next button clicked")
                break

    def countries(self):
        self.waitFl(self._countries_caret, "xpath")
        self.clickOnCountryList()
        self.selectCountries()
        time.sleep(5)
        self.clickCountriesNextButton()

    def interest(self):
        self.waitFl(self._ad_spotify_artists)
        self.spArtistSendKeys("lata")


        for i in range(51):
             if i > 49:
                 break
             time.sleep(2)
             if self.checkLoaderElement(self._interest_loader_profile, "xpath") == True:
                 self.clickInterestArtist1()
                 self.getElement(self._ad_spotify_artists).clear()
                 break

        self.spArtistSendKeys("lata")
        for i in range(51):
            if i > 49:
                break
            time.sleep(2)
            if self.checkLoaderElement(self._interest_loader_profile, "xpath") == True:
                self.clickInterestArtist2()
                self.getElement(self._ad_spotify_artists).clear()
                break

        self.spArtistSendKeys("lata")
        for i in range(51):
            if i > 49:
                break
            time.sleep(2)
            if self.checkLoaderElement(self._interest_loader_profile, "xpath") == True:
                self.clickInterestArtist3()
                self.getElement(self._ad_spotify_artists).clear()
                break
        self.waitFl(self._interest_button)
        self.clickGenerateInterestButton()

        for i in range(51):
            if i > 49:
                break
            time.sleep(2)
            if self.checkLoaderElement(self._interest_generate_profile, "xpath") == True:
                self.clickInterestNextButton()
                break

    def budget(self):
        # self.waitFl(self._budget_caret, "xpath")
        # self.clickOnBudget()
        # self.selectBudgetAmount()
        # time.sleep(15)

        self.clickBudgetNextButton()

    def advance(self):
        time.sleep(2)
        self.waitFl(self._advance_min_age_caret, "xpath")
        self.clickOnSelectMinAge()
        self.selectMinAge()
        time.sleep(2)
        self.waitFl(self._advance_max_age_caret, "xpath")
        self.clickOnSelectMaxAge()
        self.selectMaxAge()
        time.sleep(2)
        self.waitFl(self._advance_gender_caret, "xpath")
        self.clickOnSelectGender()
        self.selectGender()
        self.overRideTextSendKeys("great music")
        self.waitFl(self._advance_next_button)
        time.sleep(5)
        self.clickAdvancetNextButton()

    def confirmation(self):

        self.waitFl(self._common_terms, "xpath")
        self.clickCommonTerms()
        self.waitFl(self._facebook_terms, "xpath")
        self.clickFbTerms()
        self.waitFl(self._hypeddit_terms, "xpath")
        self.clickHypedditTerms()
        self.clickDraftNextButton()
