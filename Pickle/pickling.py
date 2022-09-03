import pickle


def save_imelda():
    """ saves a tuple as binary file """
    imelda = ('More Mayhem',
              'IMelda May',
              '2011',
              ((1, 'Pullling the rug'),
               (2, 'Psycho'),
               (3, 'Mayhem'),
               (4, 'Kentish Town Waltz'),
               ))

    with open("imelda.pickle", "wb") as pickle_file:
        pickle.dump(imelda, pickle_file)


def read_imelda():
    """ Reads the imelda file and print out the objekt. """
    with open("imelda.pickle", "rb") as imelda_format:
        imelda2 = pickle.load(imelda_format)

    print(imelda2)
    album, artist, year, track_list = imelda2

    print(album)
    print(artist)
    print(year)
    for track in track_list:
        track_number, track_title = track
        print(track_number, track_title)


def save_multiple_objekt_pickle():
    """ pickle and saves a tuple as binary file """
    imelda = ('More Mayhem',
              'IMelda May',
              '2011',
              ((1, 'Pullling the rug'),
               (2, 'Psycho'),
               (3, 'Mayhem'),
               (4, 'Kentish Town Waltz'),
               ))

    even = list(range(0, 10, 2))
    odd = list(range(1, 10, 2))

    with open("imelda.pickle", "wb") as pickle_file:
        pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
        pickle.dump(even, pickle_file, protocol=0)
        pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
        pickle.dump(2_998_302, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)


def read_multiple_objekt_pickle():
    """ Reads the imelda file and print out the objekt. """
    with open("imelda.pickle", "rb") as imelda_format:
        # must be in the same order as it was saved. **IMPORTANT**
        imelda2 = pickle.load(imelda_format)
        even_list = pickle.load(imelda_format)
        odd_list = pickle.load(imelda_format)
        number = pickle.load(imelda_format)

    print(imelda2)
    album, artist, year, track_list = imelda2

    print(album)
    print(artist)
    print(year)
    for track in track_list:
        track_number, track_title = track
        print(track_number, track_title)

    print('=' * 40)

    for i in even_list:
        print(i)

    print('=' * 40)

    for i in odd_list:
        print(i)

    print('=' * 40)

    print(number)


def main() -> None:
    """ The main function run as module"""
    # read_imelda()
    save_multiple_objekt_pickle()
    read_multiple_objekt_pickle()

    # Important the pickle protocols aren't backwards compatible.
    # version 4 protocol can't be read for all python versions.
    # protocol=0 Human readable
    # protocol=1 First binary all version of Python should be able to unpickle data.
    # protocol=2 Pickle classes mor efficiently
    # protocol=3 Default protocol if noting else is specified.
    # Don't use pickling to store data from the internet. or other untrusted sourses.
    # pickle.loads(b"cos\nsystem\n(S'rm imelda.pickle'\ntR.") this file del i file,
    # think of this of loading a file can destroy your system.
    #
    # The problem is that pickle loads all information in to the computers' memory.
    # There for this is pickle not the best choice for larger data and objects.
    # the shelve module is better choice for this.


if __name__ == '__main__':
    main()
