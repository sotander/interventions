# get conversations: messages groupped by userid, threadid, convid
GET_CONVERSATIONS_EACL_TS1_NHOT_CS = '''select
    array_agg(s.line_text::TEXT order by line_num asc) as texts,
    array_agg(s.chi_gs_multi_nhot::SMALLINT[] order by line_num asc) as gs,
    array_agg(s.author::TEXT order by line_num asc) as author,
    user_id, thread_id, conv_id
from messenger s
where s.is_annotated_tagset_0 is true or s.is_annotated_tagset_1 is true
group by s.user_id, s.thread_id, s.conv_id;
'''

# get conversations: messages groupped by userid, threadid, convid
# NEFUNGUJE
GET_EN_CONVERSATIONS_EACL_TS1_CERTAIN_NHOT = '''select
    array_agg(s.line_text_en::TEXT order by line_num asc) as texts,
    array_agg(s.eacl_gs_ts1_certain_multi_nhot::SMALLINT[] order by line_num asc) as gs,
    array_agg(s.author::TEXT order by line_num asc) as author,
    user_id, thread_id, conv_id
from messenger s
where s.is_annotated_tagset_1 is true
group by s.user_id, s.thread_id, s.conv_id;
'''

