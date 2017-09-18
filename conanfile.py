from conans import ConanFile


class BoostConan(ConanFile):
    name = "Boost"
    version = "1.64.0"
    settings = "os", "arch", "compiler", "build_type"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    default_options = "shared=False"
    options = {"shared": [True, False]}
    build_requires = "Boost.Generator/1.64.0@bincrafters/stable" 
    requires = "Boost.Accumulators/1.64.0@bincrafters/stable", \
        "Boost.Algorithm/1.64.0@bincrafters/stable", \
        "Boost.Align/1.64.0@bincrafters/stable", \
        "Boost.Any/1.64.0@bincrafters/stable", \
        "Boost.Array/1.64.0@bincrafters/stable", \
        "Boost.Asio/1.64.0@bincrafters/stable", \
        "Boost.Assert/1.64.0@bincrafters/stable", \
        "Boost.Assign/1.64.0@bincrafters/stable", \
        "Boost.Atomic/1.64.0@bincrafters/stable", \
        "Boost.Bimap/1.64.0@bincrafters/stable", \
        "Boost.Bind/1.64.0@bincrafters/stable", \
        "Boost.Chrono/1.64.0@bincrafters/stable", \
        "Boost.Circular_Buffer/1.64.0@bincrafters/stable", \
        "Boost.Compatibility/1.64.0@bincrafters/stable", \
        "Boost.Compute/1.64.0@bincrafters/stable", \
        "Boost.Concept_Check/1.64.0@bincrafters/stable", \
        "Boost.Config/1.64.0@bincrafters/stable", \
        "Boost.Container/1.64.0@bincrafters/stable", \
        "Boost.Context/1.64.0@bincrafters/stable", \
        "Boost.Conversion/1.64.0@bincrafters/stable", \
        "Boost.Convert/1.64.0@bincrafters/stable", \
        "Boost.Core/1.64.0@bincrafters/stable", \
        "Boost.Coroutine/1.64.0@bincrafters/stable", \
        "Boost.Coroutine2/1.64.0@bincrafters/stable", \
        "Boost.Crc/1.64.0@bincrafters/stable", \
        "Boost.Date_Time/1.64.0@bincrafters/stable", \
        "Boost.Detail/1.64.0@bincrafters/stable", \
        "Boost.Disjoint_Sets/1.64.0@bincrafters/stable", \
        "Boost.Dll/1.64.0@bincrafters/stable", \
        "Boost.Dynamic_Bitset/1.64.0@bincrafters/stable", \
        "Boost.Endian/1.64.0@bincrafters/stable", \
        "Boost.Exception/1.64.0@bincrafters/stable", \
        "Boost.Fiber/1.64.0@bincrafters/stable", \
        "Boost.Filesystem/1.64.0@bincrafters/stable", \
        "Boost.Flyweight/1.64.0@bincrafters/stable", \
        "Boost.Foreach/1.64.0@bincrafters/stable", \
        "Boost.Format/1.64.0@bincrafters/stable", \
        "Boost.Function/1.64.0@bincrafters/stable", \
        "Boost.Function_Types/1.64.0@bincrafters/stable", \
        "Boost.Functional/1.64.0@bincrafters/stable", \
        "Boost.Fusion/1.64.0@bincrafters/stable", \
        "Boost.Geometry/1.64.0@bincrafters/stable", \
        "Boost.Gil/1.64.0@bincrafters/stable", \
        "Boost.Graph/1.64.0@bincrafters/stable", \
        "Boost.Graph_Parallel/1.64.0@bincrafters/stable", \
        "Boost.Hana/1.64.0@bincrafters/stable", \
        "Boost.Heap/1.64.0@bincrafters/stable", \
        "Boost.Icl/1.64.0@bincrafters/stable", \
        "Boost.Integer/1.64.0@bincrafters/stable", \
        "Boost.Interprocess/1.64.0@bincrafters/stable", \
        "Boost.Intrusive/1.64.0@bincrafters/stable", \
        "Boost.Io/1.64.0@bincrafters/stable", \
        "Boost.Iostreams/1.64.0@bincrafters/stable", \
        "Boost.Iterator/1.64.0@bincrafters/stable", \
        "Boost.Lambda/1.64.0@bincrafters/stable", \
        "Boost.Level5Group/1.64.0@bincrafters/stable", \
        "Boost.Lexical_Cast/1.64.0@bincrafters/stable", \
        "Boost.Local_Function/1.64.0@bincrafters/stable", \
        "Boost.Locale/1.64.0@bincrafters/stable", \
        "Boost.Lockfree/1.64.0@bincrafters/stable", \
        "Boost.Log/1.64.0@bincrafters/stable", \
        "Boost.Logic/1.64.0@bincrafters/stable", \
        "Boost.Math/1.64.0@bincrafters/stable", \
        "Boost.Metaparse/1.64.0@bincrafters/stable", \
        "Boost.Move/1.64.0@bincrafters/stable", \
        "Boost.Mpi/1.64.0@bincrafters/stable", \
        "Boost.Mpl/1.64.0@bincrafters/stable", \
        "Boost.Msm/1.64.0@bincrafters/stable", \
        "Boost.Multi_Array/1.64.0@bincrafters/stable", \
        "Boost.Multi_Index/1.64.0@bincrafters/stable", \
        "Boost.Multiprecision/1.64.0@bincrafters/stable", \
        "Boost.Numeric_Conversion/1.64.0@bincrafters/stable", \
        "Boost.Numeric_Interval/1.64.0@bincrafters/stable", \
        "Boost.Numeric_Odeint/1.64.0@bincrafters/stable", \
        "Boost.Numeric_Ublas/1.64.0@bincrafters/stable", \
        "Boost.Optional/1.64.0@bincrafters/stable", \
        "Boost.Parameter/1.64.0@bincrafters/stable", \
        "Boost.Phoenix/1.64.0@bincrafters/stable", \
        "Boost.Polygon/1.64.0@bincrafters/stable", \
        "Boost.Pool/1.64.0@bincrafters/stable", \
        "Boost.Predef/1.64.0@bincrafters/stable", \
        "Boost.Preprocessor/1.64.0@bincrafters/stable", \
        "Boost.Process/1.64.0@bincrafters/stable", \
        "Boost.Program_Options/1.64.0@bincrafters/stable", \
        "Boost.Property_Map/1.64.0@bincrafters/stable", \
        "Boost.Property_Tree/1.64.0@bincrafters/stable", \
        "Boost.Proto/1.64.0@bincrafters/stable", \
        "Boost.Ptr_Container/1.64.0@bincrafters/stable", \
        "Boost.Python/1.64.0@bincrafters/stable", \
        "Boost.Qvm/1.64.0@bincrafters/stable", \
        "Boost.Random/1.64.0@bincrafters/stable", \
        "Boost.Range/1.64.0@bincrafters/stable", \
        "Boost.Ratio/1.64.0@bincrafters/stable", \
        "Boost.Rational/1.64.0@bincrafters/stable", \
        "Boost.Regex/1.64.0@bincrafters/stable", \
        "Boost.Scope_Exit/1.64.0@bincrafters/stable", \
        "Boost.Serialization/1.64.0@bincrafters/stable", \
        "Boost.Signals/1.64.0@bincrafters/stable", \
        "Boost.Signals2/1.64.0@bincrafters/stable", \
        "Boost.Smart_Ptr/1.64.0@bincrafters/stable", \
        "Boost.Sort/1.64.0@bincrafters/stable", \
        "Boost.Spirit/1.64.0@bincrafters/stable", \
        "Boost.Statechart/1.64.0@bincrafters/stable", \
        "Boost.Static_Assert/1.64.0@bincrafters/stable", \
        "Boost.System/1.64.0@bincrafters/stable", \
        "Boost.Test/1.64.0@bincrafters/stable", \
        "Boost.Thread/1.64.0@bincrafters/stable", \
        "Boost.Throw_Exception/1.64.0@bincrafters/stable", \
        "Boost.Timer/1.64.0@bincrafters/stable", \
        "Boost.Tokenizer/1.64.0@bincrafters/stable", \
        "Boost.Tti/1.64.0@bincrafters/stable", \
        "Boost.Tuple/1.64.0@bincrafters/stable", \
        "Boost.Type_Erasure/1.64.0@bincrafters/stable", \
        "Boost.Type_Index/1.64.0@bincrafters/stable", \
        "Boost.Type_Traits/1.64.0@bincrafters/stable", \
        "Boost.Typeof/1.64.0@bincrafters/stable", \
        "Boost.Units/1.64.0@bincrafters/stable", \
        "Boost.Unordered/1.64.0@bincrafters/stable", \
        "Boost.Utility/1.64.0@bincrafters/stable", \
        "Boost.Uuid/1.64.0@bincrafters/stable", \
        "Boost.Variant/1.64.0@bincrafters/stable", \
        "Boost.Vmd/1.64.0@bincrafters/stable", \
        "Boost.Wave/1.64.0@bincrafters/stable", \
        "Boost.Winapi/1.64.0@bincrafters/stable", \
        "Boost.Xpressive/1.64.0@bincrafters/stable", \


