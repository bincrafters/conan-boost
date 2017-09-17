from conans import ConanFile


class BoostConan(ConanFile):
    name = "Boost"
    version = "1.65.1"
    settings = "os", "arch", "compiler", "build_type"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    default_options = "shared=False"
    options = {"shared": [True, False]}
    build_requires = "Boost.Generator/0.0.1@bincrafters/testing" 
    requires = "Boost.Accumulators/1.65.1@bincrafters/testing", \
        "Boost.Algorithm/1.65.1@bincrafters/testing", \
        "Boost.Align/1.65.1@bincrafters/testing", \
        "Boost.Any/1.65.1@bincrafters/testing", \
        "Boost.Array/1.65.1@bincrafters/testing", \
        "Boost.Asio/1.65.1@bincrafters/testing", \
        "Boost.Assert/1.65.1@bincrafters/testing", \
        "Boost.Assign/1.65.1@bincrafters/testing", \
        "Boost.Atomic/1.65.1@bincrafters/testing", \
        "Boost.Bimap/1.65.1@bincrafters/testing", \
        "Boost.Bind/1.65.1@bincrafters/testing", \
        "Boost.Chrono/1.65.1@bincrafters/testing", \
        "Boost.Circular_Buffer/1.65.1@bincrafters/testing", \
        "Boost.Compatibility/1.65.1@bincrafters/testing", \
        "Boost.Compute/1.65.1@bincrafters/testing", \
        "Boost.Concept_Check/1.65.1@bincrafters/testing", \
        "Boost.Config/1.65.1@bincrafters/testing", \
        "Boost.Container/1.65.1@bincrafters/testing", \
        "Boost.Context/1.65.1@bincrafters/testing", \
        "Boost.Conversion/1.65.1@bincrafters/testing", \
        "Boost.Convert/1.65.1@bincrafters/testing", \
        "Boost.Core/1.65.1@bincrafters/testing", \
        "Boost.Coroutine/1.65.1@bincrafters/testing", \
        "Boost.Coroutine2/1.65.1@bincrafters/testing", \
        "Boost.Crc/1.65.1@bincrafters/testing", \
        "Boost.Date_Time/1.65.1@bincrafters/testing", \
        "Boost.Detail/1.65.1@bincrafters/testing", \
        "Boost.Disjoint_Sets/1.65.1@bincrafters/testing", \
        "Boost.Dll/1.65.1@bincrafters/testing", \
        "Boost.Dynamic_Bitset/1.65.1@bincrafters/testing", \
        "Boost.Endian/1.65.1@bincrafters/testing", \
        "Boost.Exception/1.65.1@bincrafters/testing", \
        "Boost.Fiber/1.65.1@bincrafters/testing", \
        "Boost.Filesystem/1.65.1@bincrafters/testing", \
        "Boost.Flyweight/1.65.1@bincrafters/testing", \
        "Boost.Foreach/1.65.1@bincrafters/testing", \
        "Boost.Format/1.65.1@bincrafters/testing", \
        "Boost.Function/1.65.1@bincrafters/testing", \
        "Boost.Function_Types/1.65.1@bincrafters/testing", \
        "Boost.Functional/1.65.1@bincrafters/testing", \
        "Boost.Fusion/1.65.1@bincrafters/testing", \
        "Boost.Geometry/1.65.1@bincrafters/testing", \
        "Boost.Gil/1.65.1@bincrafters/testing", \
        "Boost.Graph/1.65.1@bincrafters/testing", \
        "Boost.Graph_Parallel/1.65.1@bincrafters/testing", \
        "Boost.Hana/1.65.1@bincrafters/testing", \
        "Boost.Heap/1.65.1@bincrafters/testing", \
        "Boost.Icl/1.65.1@bincrafters/testing", \
        "Boost.Integer/1.65.1@bincrafters/testing", \
        "Boost.Interprocess/1.65.1@bincrafters/testing", \
        "Boost.Intrusive/1.65.1@bincrafters/testing", \
        "Boost.Io/1.65.1@bincrafters/testing", \
        "Boost.Iostreams/1.65.1@bincrafters/testing", \
        "Boost.Iterator/1.65.1@bincrafters/testing", \
        "Boost.Lambda/1.65.1@bincrafters/testing", \
        "Boost.Level5Group/1.65.1@bincrafters/testing", \
        "Boost.Lexical_Cast/1.65.1@bincrafters/testing", \
        "Boost.Local_Function/1.65.1@bincrafters/testing", \
        "Boost.Locale/1.65.1@bincrafters/testing", \
        "Boost.Lockfree/1.65.1@bincrafters/testing", \
        "Boost.Log/1.65.1@bincrafters/testing", \
        "Boost.Logic/1.65.1@bincrafters/testing", \
        "Boost.Math/1.65.1@bincrafters/testing", \
        "Boost.Metaparse/1.65.1@bincrafters/testing", \
        "Boost.Move/1.65.1@bincrafters/testing", \
        "Boost.Mpi/1.65.1@bincrafters/testing", \
        "Boost.Mpl/1.65.1@bincrafters/testing", \
        "Boost.Msm/1.65.1@bincrafters/testing", \
        "Boost.Multi_Array/1.65.1@bincrafters/testing", \
        "Boost.Multi_Index/1.65.1@bincrafters/testing", \
        "Boost.Multiprecision/1.65.1@bincrafters/testing", \
        "Boost.Numeric_Conversion/1.65.1@bincrafters/testing", \
        "Boost.Numeric_Interval/1.65.1@bincrafters/testing", \
        "Boost.Numeric_Odeint/1.65.1@bincrafters/testing", \
        "Boost.Numeric_Ublas/1.65.1@bincrafters/testing", \
        "Boost.Optional/1.65.1@bincrafters/testing", \
        "Boost.Parameter/1.65.1@bincrafters/testing", \
        "Boost.Phoenix/1.65.1@bincrafters/testing", \
        "Boost.Polygon/1.65.1@bincrafters/testing", \
        "Boost.Pool/1.65.1@bincrafters/testing", \
        "Boost.Predef/1.65.1@bincrafters/testing", \
        "Boost.Preprocessor/1.65.1@bincrafters/testing", \
        "Boost.Process/1.65.1@bincrafters/testing", \
        "Boost.Program_Options/1.65.1@bincrafters/testing", \
        "Boost.Property_Map/1.65.1@bincrafters/testing", \
        "Boost.Property_Tree/1.65.1@bincrafters/testing", \
        "Boost.Proto/1.65.1@bincrafters/testing", \
        "Boost.Ptr_Container/1.65.1@bincrafters/testing", \
        "Boost.Python/1.65.1@bincrafters/testing", \
        "Boost.Qvm/1.65.1@bincrafters/testing", \
        "Boost.Random/1.65.1@bincrafters/testing", \
        "Boost.Range/1.65.1@bincrafters/testing", \
        "Boost.Ratio/1.65.1@bincrafters/testing", \
        "Boost.Rational/1.65.1@bincrafters/testing", \
        "Boost.Regex/1.65.1@bincrafters/testing", \
        "Boost.Scope_Exit/1.65.1@bincrafters/testing", \
        "Boost.Serialization/1.65.1@bincrafters/testing", \
        "Boost.Signals/1.65.1@bincrafters/testing", \
        "Boost.Signals2/1.65.1@bincrafters/testing", \
        "Boost.Smart_Ptr/1.65.1@bincrafters/testing", \
        "Boost.Sort/1.65.1@bincrafters/testing", \
        "Boost.Spirit/1.65.1@bincrafters/testing", \
        "Boost.Statechart/1.65.1@bincrafters/testing", \
        "Boost.Static_Assert/1.65.1@bincrafters/testing", \
        "Boost.System/1.65.1@bincrafters/testing", \
        "Boost.Test/1.65.1@bincrafters/testing", \
        "Boost.Thread/1.65.1@bincrafters/testing", \
        "Boost.Throw_Exception/1.65.1@bincrafters/testing", \
        "Boost.Timer/1.65.1@bincrafters/testing", \
        "Boost.Tokenizer/1.65.1@bincrafters/testing", \
        "Boost.Tti/1.65.1@bincrafters/testing", \
        "Boost.Tuple/1.65.1@bincrafters/testing", \
        "Boost.Type_Erasure/1.65.1@bincrafters/testing", \
        "Boost.Type_Index/1.65.1@bincrafters/testing", \
        "Boost.Type_Traits/1.65.1@bincrafters/testing", \
        "Boost.Typeof/1.65.1@bincrafters/testing", \
        "Boost.Units/1.65.1@bincrafters/testing", \
        "Boost.Unordered/1.65.1@bincrafters/testing", \
        "Boost.Utility/1.65.1@bincrafters/testing", \
        "Boost.Uuid/1.65.1@bincrafters/testing", \
        "Boost.Variant/1.65.1@bincrafters/testing", \
        "Boost.Vmd/1.65.1@bincrafters/testing", \
        "Boost.Wave/1.65.1@bincrafters/testing", \
        "Boost.Winapi/1.65.1@bincrafters/testing", \
        "Boost.Xpressive/1.65.1@bincrafters/testing", \


