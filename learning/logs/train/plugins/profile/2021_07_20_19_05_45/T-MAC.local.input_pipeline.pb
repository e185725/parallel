	?~j?t?0@?~j?t?0@!?~j?t?0@	K??9?E@K??9?E@!K??9?E@"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$?~j?t?0@??(\?µ?A㥛? 0#@YJ+?@*      Q@     #?@2?
cIterator::Model::MaxIntraOpParallelism::Prefetch::RebatchV2::BatchV2::Shuffle::MemoryCacheImpl::Map?5^?I?%@!?Uo???B@)??K7??%@1? 'aߝB@:Preprocessing2T
Iterator::Prefetch::Generator??MbX@!y?5?W3@)??MbX@1y?5?W3@:Preprocessing2?
ZIterator::Model::MaxIntraOpParallelism::Prefetch::RebatchV2::BatchV2::Shuffle::MemoryCache?5^?I%@!5mvq`8B@)?5^?I?@1?].?2@:Preprocessing2?
?Iterator::Model::MaxIntraOpParallelism::Prefetch::RebatchV2::BatchV2::Shuffle::MemoryCacheImpl::Map::Prefetch::MemoryCacheImpl::ParallelMapV2::ParallelInterleaveV4D?l???@!ƨBR?!@)D?l???@1ƨBR?!@:Preprocessing2?
?Iterator::Model::MaxIntraOpParallelism::Prefetch::RebatchV2::BatchV2::Shuffle::MemoryCacheImpl::Map::Prefetch::MemoryCacheImpl::ParallelMapV2::ParallelInterleaveV4[0]::FlatMap?x?&1@!???|@)??Q?? @1
"P7??@:Preprocessing2?
^Iterator::Model::MaxIntraOpParallelism::Prefetch::RebatchV2::BatchV2::Shuffle::MemoryCacheImpl????S@!?D?ϣ14@)?/?$??1??W?3@:Preprocessing2?
zIterator::Model::MaxIntraOpParallelism::Prefetch::RebatchV2::BatchV2::Shuffle::MemoryCacheImpl::Map::Prefetch::MemoryCache#??~j???!A?F<?@)??? ?r??1?|?i?@:Preprocessing2?
?Iterator::Model::MaxIntraOpParallelism::Prefetch::RebatchV2::BatchV2::Shuffle::MemoryCacheImpl::Map::Prefetch::MemoryCacheImpl::ParallelMapV2? ?rh???!??a_j??)? ?rh???1??a_j??:Preprocessing2F
Iterator::Model^?I+??!????.??)^?I+??1????.??:Preprocessing2?
mIterator::Model::MaxIntraOpParallelism::Prefetch::RebatchV2::BatchV2::Shuffle::MemoryCacheImpl::Map::Prefetcho??ʡ??!g?˹??)o??ʡ??1g?˹??:Preprocessing2g
0Iterator::Model::MaxIntraOpParallelism::Prefetchsh??|???!?3??d??)sh??|???1?3??d??:Preprocessing2?
~Iterator::Model::MaxIntraOpParallelism::Prefetch::RebatchV2::BatchV2::Shuffle::MemoryCacheImpl::Map::Prefetch::MemoryCacheImplX9??v???!Ɓ?r?z??)?Zd;??1CR?8	??:Preprocessing2?
?Iterator::Model::MaxIntraOpParallelism::Prefetch::RebatchV2::BatchV2::Shuffle::MemoryCacheImpl::Map::Prefetch::MemoryCacheImpl::ParallelMapV2::ParallelInterleaveV4[0]::FlatMap[0]::TFRecord?? ?rh??!؞ u#??)?? ?rh??1؞ u#??:Advanced file read2?
MIterator::Model::MaxIntraOpParallelism::Prefetch::RebatchV2::BatchV2::Shuffle\???(?@!??\??2@)???x?&??1Uo??????:Preprocessing2I
Iterator::Prefetch9??v????!???.??)9??v????1???.??:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
host?Your program is HIGHLY input-bound because 42.0% of the total step time sampled is waiting for input. Therefore, you should first focus on reducing the input time.no*no9K??9?E@I?>i?0?L@Zno>Look at Section 3 for the breakdown of input time on the host.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	??(\?µ???(\?µ?!??(\?µ?      ??!       "      ??!       *      ??!       2	㥛? 0#@㥛? 0#@!㥛? 0#@:      ??!       B      ??!       J	J+?@J+?@!J+?@R      ??!       Z	J+?@J+?@!J+?@b      ??!       JCPU_ONLYYK??9?E@b q?>i?0?L@