try:
    import pyaudio, wave
    from pydub import AudioSegment
except:
    print("no pyaudio")


class MapperF:
    def __init__(self):
        self.mapping = {'p':'vls_blb_psv_f.wav',
                        'b':'vcd_blb_psv_f.wav',
                        't':'vls_alv_psv_f.wav',
                        'd':'vcd_alv_psv_f.wav',
                        'ʈ':'vls_ret_psv_f.wav',
                        'ɖ':'vcd_ret_psv_f.wav',
                        'c':'vls_plt_psv_f.wav',
                        'ɟ':'vcd_plt_psv_f.wav',
                        'k':'vls_vlr_psv_f.wav',
                        'ɡ':'vcd_vlr_psv_f.wav',
                        'g':'vcd_vlr_psv_f.wav',
                        'q':'vls_uvl_psv_f.wav',
                        'ɢ':'vcd_uvl_psv_f.wav',
                        'ʔ':'vls_glt_psv_f.wav',
                        'm':'vcd_blb_nsl_f.wav',
                        'ɱ':'vcd_lbd_nsl_f.wav',
                        'n':'vcd_alv_nsl_f.wav',
                        'ɲ':'vcd_plt_nsl_f.wav',
                        'ɳ':'vcd_ret_nsl_f.wav',
                        'ŋ':'vcd_vlr_nsl_f.wav',
                        'ɴ':'vcd_uvl_nsl_f.wav',
                        'ʙ':'vcd_blb_trl_f.wav',
                        'r':'vcd_alv_trl_f.wav',
                        'ʀ':'vcd_uvl_trl_f.wav',
                        'ⱱ':'vcd_lbd_tap_f.wav',
                        'ɾ':'vcd_alv_tap_f.wav',
                        'ɽ':'vcd_ret_tap_f.wav',
                        'ɸ':'vls_blb_fri_f.wav',
                        'β':'vcd_blb_fri_f.wav',
                        'f':'vls_lbd_fri_f.wav',
                        'v':'vcd_lbd_fri_f.wav',
                        'θ':'vls_dtl_fri_f.wav',
                        'ð':'vcd_dtl_fri_f.wav',
                        's':'vls_alv_fri_f.wav',
                        'z':'vcd_alv_fri_f.wav',
                        'ʃ':'vls_pav_fri_f.wav',
                        'ʒ':'vcd_pav_fri_f.wav',
                        'ʂ':'vls_ret_fri_f.wav',
                        'ʐ':'vcd_ret_fri_f.wav',
                        'ç':'vls_plt_fri_f.wav',
                        'ʝ':'vcd_plt_fri_f.wav',
                        'x':'vls_vlr_fri_f.wav',
                        'ɣ':'vcd_vlr_fri_f.wav',
                        'χ':'vls_uvl_fri_f.wav',
                        'ʁ':'vcd_uvl_fri_f.wav',
                        'h':'vls_glt_fri_f.wav',
                        'ʕ':'vcd_pha_fri_f.wav',
                        'ħ':'vls_pha_fri_f.wav',
                        'ɦ':'vcd_glt_fri_f.wav',
                        'ɬ':'vls_alv_lfr_f.wav',
                        'ɮ':'vcd_alv_lfr_f.wav',
                        'ʋ':'vcd_lbd_apx_f.wav',
                        'ɹ':'vcd_alv_apx_f.wav',
                        'ɻ':'vcd_ret_apx_f.wav',
                        'j':'vcd_plt_apx_f.wav',
                        'ɰ':'vcd_vlr_apx_f.wav',
                        'l':'vcd_alv_lap_f.wav',
                        'ɭ':'vcd_ret_lap_f.wav',
                        'ʎ':'vcd_plt_lap_f.wav',
                        'ʟ':'vcd_vlr_lap_f.wav',
                        'ʘ':'vls_blb_clk_f.wav',
                        '|':'vls_dtl_clk_f.wav',
                        'ǂ':'vls_pav_clk_f.wav',
                        'ǁ':'vls_avl_clk_f.wav', #alveolo-lateral
                        '!':'vls_alv_clk_f.wav',
                        'ɓ':'vcd_blb_imp_f.wav',
                        'ɗ':'vcd_alv_imp_f.wav',
                        'ɠ':'vcd_vlr_imp_f.wav',
                        'ʄ':'vcd_plt_imp_f.wav',
                        'ʛ':'vcd_uvl_imp_f.wav',
                        'p\'':'vls_blb_eje_f.wav',
                        't\'':'vls_alv_eje_f.wav',
                        'k\'':'vls_vlr_eje_f.wav',
                        's\'':'vls_alv_sej_f.wav', #sibilant ejective
                        'ʍ':'vls_lbv_apx_f.wav', #labio-velar
                        'w':'vcd_lbv_apx_f.wav',
                        'ɥ':'vcd_lpl_apx_f.wav', #labio-palatal
                        'ʜ':'vls_epi_trl_f.wav',
                        'ʢ':'vcd_epi_trl_f.wav',
                        'ʡ':'vcd_epi_psv_f.wav',
                        'ɕ':'vls_avp_fri_f.wav', #alveolo-palatal
                        'ʑ':'vcd_avp_fri_f.wav',
                        'ɺ':'vcd_avl_tap_f.wav',
                        'ɧ':'vls_vpa_fri_f.wav', #velo-postalveolar
                        'kp':'vls_vbl_psv_f.wav', #velo-bilabial
                        'ts':'vls_alv_afr_f.wav', #affricate
                        'i':'cl_fr_u_f.wav',
                        'y':'cl_fr_r_f.wav',
                        'ɨ':'cl_ce_u_f.wav',
                        'ʉ':'cl_ce_r_f.wav',
                        'ɯ':'cl_bk_u_f.wav',
                        'u':'cl_bk_r_f.wav',
                        'ɪ':'nc_nf_u_f.wav',
                        'ʏ':'nc_nf_r_f.wav',
                        'ʊ':'nc_nb_r_f.wav',
                        'e':'cm_fr_u_f.wav',
                        'ø':'cm_fr_r_f.wav',
                        'ɘ':'cm_ce_u_f.wav',
                        'ɵ':'cm_ce_r_f.wav',
                        'ɤ':'cm_bk_u_f.wav',
                        'o':'cm_bk_r_f.wav',
                        'ə':'mi_ce_u_f.wav',
                        'ɛ':'om_fr_u_f.wav',
                        'œ':'om_fr_r_f.wav',
                        'ɜ':'om_ce_u_f.wav',
                        'ɞ':'om_ce_r_f.wav',
                        'ʌ':'om_bk_u_f.wav',
                        'ɔ':'om_bk_r_f.wav',
                        'æ':'no_fr_u_f.wav',
                        'ɐ':'no_ce_u_f.wav',
                        'a':'op_fr_u_f.wav',
                        'ɶ':'op_fr_r_f.wav',
                        'ɑ':'op_bk_u_f.wav',
                        'ɒ':'op_bk_r_f.wav',
                        'ʰ':'aspirant_f.wav',
                        'nvls':'nvls.wav',
                        'dvls':'dvls.wav',
                        'svcd':'svcd.wav',
                        'tvcd':'tvcd.wav',
                        'tasp':'tasp.wav',
                        'dasp':'dasp.wav',
                        'omrd':'omrd.wav',
                        'olrd':'olrd.wav',
                        'uadv':'uadv.wav',
                        'eret':'eret.wav',
                        'aret':'aret.wav',
                        'ectr':'ectr.wav',
                        'emct':'emct.wav',
                        'nsyl':'nsyl.wav',
                        'erho':'erho.wav',
                        'bbre':'bbre.wav',
                        'abre':'abre.wav',
                        'bcre':'bcre.wav',
                        'acre':'acre.wav',
                        'tlnl':'tlnl.wav',
                        'dlnl':'dlnl.wav',
                        'tlab':'tlab.wav',
                        'dlab':'dlab.wav',
                        'tplt':'tplt.wav',
                        'dplt':'dplt.wav',
                        'tvlr':'tvlr.wav',
                        'dvlr':'dvlr.wav',
                        'tpha':'tpha.wav',
                        'dpha':'dpha.wav',
                        'lvlr':'lvlr.wav',
                        'ersd':'ersd.wav',
                        'rrsd':'rrsd.wav',
                        'elwr':'elwr.wav',
                        'vlwr':'vlwr.wav',
                        'eatr':'eatr.wav',
                        'ertr':'ertr.wav',
                        'tdtl':'tdtl.wav',
                        'ddtl':'ddtl.wav',
                        'tapc':'tapc.wav',
                        'dapc':'dapc.wav',
                        'tlam':'tlam.wav',
                        'dlam':'dlam.wav',
                        'ensl':'ensl.wav',
                        'dnsr':'dnsr.wav',
                        'dlar':'dlar.wav',
                        'dnau':'dnau.wav',
                        'elng':'elng.wav',
                        'ehln':'ehln.wav',
                        'esht':'esht.wav',
                        'e5':'e5.wav',
                        'e4':'e4.wav',
                        'e3':'e3.wav',
                        'e2':'e2.wav',
                        'e1':'e1.wav',
                        'e15':'e15.wav',
                        'e51':'e51.wav',
                        'e35':'e35.wav',
                        'e13':'e13.wav',
                        'e454':'e454.wav',
                        }
        def addMapper(self, key, sound_file):
            if key not in self.mapping:
                self.mapping[key] = [sound_file]

class AudioPlayer:
    def __init__(self):
        self.mapper = MapperF()
        
    def play_audio(self, phoneme):
        self.p = pyaudio.PyAudio()
        fn = self.mapper.mapping[phoneme]
        chunk = 1024
        try:
            f = wave.open("./sounds/" + fn,"rb")
            stream = self.p.open(format = self.p.get_format_from_width(f.getsampwidth()),  
                    channels = f.getnchannels(),  
                    rate = f.getframerate(),  
                    output = True)
            data = f.readframes(chunk)
            while data:  
                stream.write(data)  
                data = f.readframes(chunk)
            stream.stop_stream()
            stream.close()  
            self.p.terminate()
            f.close()
        except:
            print(fn + " not found")
