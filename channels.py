import time
import simplejson
from channel import BaseChannel, ChannelException,ChannelMetaClass, STATUS_BAD, STATUS_GOOD, STATUS_UGLY
from utils import *

class AlJazeeraLive(BaseChannel):
    playable = True
    short_name = 'aljazeera'
    long_name = "Al-Jazeera Live (English)"
    default_action = 'play_stream'

    def action_play_stream(self):
        self.plugin.set_stream_url("rtmp://livestfslivefs.fplive.net/livestfslive-live/ app=aljazeeraflashlive-live?videoId=747084146001&lineUpId=&pubId=665003303001&playerId=751182905001&affiliateId= playpath=aljazeera_en_veryhigh?videoId=747084146001&lineUpId=&pubId=665003303001&playerId=751182905001&affiliateId= pageurl=http://english.aljazeera.net/watch_now/ live=true")
    
        
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
        data.update({'stream_url': "rtmp://cp44679.live.edgefcs.net/live/cnn_stream4_low@2797", 'stream_number': 4, 'Title': 'CNN 3'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()
        
        
    def action_play_stream(self):
        parser = URLParser(swf_url = self.swf_url)
        self.plugin.set_stream_url(parser(self.args['stream_url']))
        
    