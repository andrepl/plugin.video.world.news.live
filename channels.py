import time
import simplejson
from channel import BaseChannel, ChannelException,ChannelMetaClass, STATUS_BAD, STATUS_GOOD, STATUS_UGLY
from utils import *

class AlJazeeraArabic(BaseChannel):
    playable = False
    short_name = 'aljazeera_ar'
    long_name = 'Al-Jazeera Live (Arabic)'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'High Definition', 'stream_url': 'rtmp://livestfslivefs.fplive.net/livestfslive-live/ playpath=aljazeera_ar_veryhigh app=aljazeeraflashlive-live swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Standard Definition', 'stream_url': 'rtmp://livestfslivefs.fplive.net/livestfslive-live/ playpath=aljazeera_ar_high app=aljazeeraflashlive-live swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Low Definition', 'stream_url': 'rtmp://livestfslivefs.fplive.net/livestfslive-live/ playpath=aljazeera_ar_low app=aljazeeraflashlive-live swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

class AlJazeeraLive(BaseChannel):
    playable = True
    short_name = 'aljazeera'
    long_name = "Al-Jazeera Live (English)"
    default_action = 'play_stream'

    def action_play_stream(self):
        self.plugin.set_stream_url("rtmp://livestfslivefs.fplive.net/livestfslive-live/ app=aljazeeraflashlive-live?videoId=747084146001&lineUpId=&pubId=665003303001&playerId=751182905001&affiliateId= playpath=aljazeera_en_veryhigh?videoId=747084146001&lineUpId=&pubId=665003303001&playerId=751182905001&affiliateId= pageurl=http://english.aljazeera.net/watch_now/ live=true")
    
        
class BBC(BaseChannel):
    playable = True
    short_name = 'bbc'
    long_name = 'BBC World News'
    
    default_action = 'play_stream' 

    def action_play_stream(self):
        self.plugin.set_stream_url('rtmp://media2.lsops.net/live/ playpath=bbcworld1_en_high.sdp swfUrl="http://www.livestation.com/flash/player/5.4/player.swf" pageUrl="http://www.livestation.com/channels/10-bbc-world-news-english" swfVfy=true live=true')
    
        
class RT(BaseChannel):
    playable = False
    short_name = 'rt'
    long_name = 'RT'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'English', 'stream_url': 'rtmp://fms5.visionip.tv/live app=live swfUrl=http://rt.com/s/swf/player5.4.viral.swf pageURL=http://rt.com/on-air/ playpath=RT_3 live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Spanish', 'stream_url': 'rtmp://rt.fms.visionip.tv/live/ app=live swfurl=http://actualidad.rt.com/swf/player.swf pageurl=http://actualidad.rt.com/mas/envivo/ playpath=RT_Spanish_3 swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Arabic', 'stream_url': 'rtmp://russiatoday.fms.visionip.tv/rt/Russia_al_yaum_1000k_1 app=rt/Russia_al_yaum_1000k_1 swfurl=http://arabic.rt.com/style/liveplayer.swf pageurl=http://arabic.rt.com/live_high playpath=1000k_1 swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])
    
class ABCNews24(BaseChannel):
    playable=True
    short_name = 'abc24'
    long_name = "ABC News 24 (Australia)"
    default_action = 'play_stream'

    def action_play_stream(self):        
        self.plugin.set_stream_url("rtmp://cp103653.live.edgefcs.net:1935/live?_fcs_vhost=cp103653.live.edgefcs.net&akmfv=1.8 playpath=international_medium@36382 swfVfy=true live=true")
    
class EuroNews(BaseChannel):
    playable = True
    short_name = 'euronews'
    long_name = 'EuroNews'
    default_action = 'play_stream'
    
    def action_play_stream(self):
	self.plugin.set_stream_url('rtmp://media2.lsops.net/live/ playpath=euronews_en_high.sdp swfUrl="http://www.livestation.com/flash/player/5.4/player.swf" pageUrl="http://www.livestation.com/channels/1-euronews-english" swfVfy=true live=true')
	
	

class NASAHD(BaseChannel):
    playable = True
    short_name = 'nasahd'
    long_name = 'NASA HD'
    default_action = 'play_stream'
    
    def action_play_stream(self):
	self.plugin.set_stream_url('rtmp://flash86.ustream.tv:1935/ustreamVideo/6540154 playpath=streams/live app=ustreamVideo/6540154 swfUrl="http://cdn1.ustream.tv/swf/4/viewer.rsl.558.swf" pageUrl="http://www.nasa.gov/multimedia/nasatv/ustream.html" live=true')

class France24(BaseChannel):
    playable = False
    short_name = 'france24'
    long_name = 'France 24'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'English', 'stream_url': 'rtmp://stream2.france24.yacast.net/france24_live/en/ playpath=f24_liveen swfUrl="http://www.france24.com/en/sites/all/modules/maison/aef_player/flash/player.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Francais', 'stream_url': 'rtmp://stream2.france24.yacast.net/france24_live/fr/ playpath=f24_livefr swfUrl="http://www.france24.com/fr/sites/all/modules/maison/aef_player/flash/player.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])
    
class CSpan(BaseChannel):
    playable = False
    short_name = 'cspan'
    long_name = 'CSPAN'
    default_action = 'list_streams'
    swf_url = 'http://www.c-span.org/cspanVideoHD.swf'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data['action'] = 'play_stream'
        data.update({'stream_url': "rtmp://cp82346.live.edgefcs.net:1935/live/CSPAN1@14845", 'Title': 'CSPAN1'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'stream_url': "rtmp://cp82347.live.edgefcs.net:1935/live/CSPAN2@14846", 'Title': 'CSPAN2'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'stream_url': "rtmp://cp82348.live.edgefcs.net:1935/live/CSPAN3@14847", 'Title': 'CSPAN3'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()
        
        
    def action_play_stream(self):
        parser = URLParser(swf_url = self.swf_url)
        self.plugin.set_stream_url(parser(self.args['stream_url']))
        
                    
class CNN(BaseChannel):
    playable = False
    short_name = 'cnn'
    long_name = 'CNN'
    default_action = 'list_streams'
    swf_url = 'http://i.cdn.turner.com/cnn/.element/apps/CNNLive/2.1.5.7/assets/swfs/LivePlayer.swf'
    

    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data['action'] = 'play_stream'
        data.update({'stream_url': "rtmp://cp44679.live.edgefcs.net/live/cnn_stream1_low@2785", 'stream_number': 1,  'Title': 'CNN 1'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'stream_url': "rtmp://cp44679.live.edgefcs.net/live/cnn_stream2_low@2787", 'stream_number': 2, 'Title': 'CNN 2'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'stream_url': "rtmp://cp44679.live.edgefcs.net/live/cnn_stream3_low@2796", 'stream_number': 3, 'Title': 'CNN 3'})
        self.plugin.add_list_item(data, is_folder=False)        
        data.update({'stream_url': "rtmp://cp44679.live.edgefcs.net/live/cnn_stream4_low@2797", 'stream_number': 4, 'Title': 'CNN 4'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()
        
        
    def action_play_stream(self):
        parser = URLParser(swf_url = self.swf_url)
        self.plugin.set_stream_url(parser(self.args['stream_url']))
        
    
