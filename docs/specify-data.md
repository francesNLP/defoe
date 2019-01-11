# Specify data to query

Spark needs to know the data which you want to run a query over. You need to create a plain-text file with a list of the paths to the data files to query.

## British Library Books dataset 

To run queries over the British Library Books dataset, the file needs a list of the paths to the zip files corresponding to the books over which the query is to be run.

For example, suppose you want to run a query over two books:

```
1510_1699/000001143_0_1-20pgs__560409_dat.zip
1510_1699/000000874_0_1-22pgs__570785_dat.zip
```

If running on your local machine, your file would be as follows, where `<BOOKS>` is the path to the directory in your home directory, where you have the data:

```
<BOOKS>/1510_1699/000001143_0_1-20pgs__560409_dat.zip
<BOOKS>/1510_1699/000000874_0_1-22pgs__570785_dat.zip
```

If running on Urika, your file would be as follows:

```
/mnt/lustre/<your-urika-username>/dch/BritishLibraryBooks/1510_1699/000001143_0_1-20pgs__560409_dat.zip
/mnt/lustre/<your-urika-username>/dch/BritishLibraryBooks/1510_1699/000000874_0_1-22pgs__570785_dat.zip
```

You can write these files by hand.

Alternatively, you can use the bash `find` command, to search for the files. For example, suppose you want to run a query over all the books, you can create a file with the paths to all the books files as follows:

* On a local machine:

```bash
find <BOOKS> -name "*.zip" > files.txt
```

* On Urika:

```bash
find /mnt/lustre/<your-urika-username>/dch/BritishLibraryBooks -name "*.zip" > files.txt
```

Suppose you want to run a query over all the books in the folder `1510_1699`. You can create a file with the paths to these books files as follows:

* On a local machine:

```bash
find <BOOKS>/1510_1699/ -name "*.zip" > files.txt
```

* On Urika:

```bash
find /mnt/lustre/<your-urika-username>/dch/BritishLibraryBooks/1510_1699 -name "*.zip" > files.txt
```

---

## British Library Newspapers dataset 

To run queries over the British Library Newspapers dataset, the file needs a list of the paths to the XML files corresponding to the newspapers over which the query is to be run.

For example, suppose you want to run a query over two newspapers:

```
xmls/0000164- The Courier and Argus/0000164_19070603.xml
xmls/0000164- The Courier and Argus/0000164_19151123.xml
```

If running on your local machine, your file would be as follows, where `<NEWSPAPERS>` is the path to the directory in your home directory, where you have the data:

```
<NEWSPAPERS>/xmls/0000164- The Courier and Argus/0000164_19070603.xml
<NEWSPAPERS>/xmls/0000164- The Courier and Argus/0000164_19151123.xml
```

If running on Urika, your file would be as follows:

```
/mnt/lustre/<your-urika-username>/blpaper/xmls/0000164- The Courier and Argus/0000164_19070603.xml
/mnt/lustre/<your-urika-username>/blpaper/xmls/0000164- The Courier and Argus/0000164_19151123.xml
```

You can write these files by hand.

Alternatively, you can use the bash `find` command, to search for the files. For example, suppose you want to run a query over all the newspapers, you can create a file with the paths to all the newspapers files as follows:

* On a local machine:

```bash
find <NEWSPAPERS>/xmls -name "*.xml" > files.txt
```

* On Urika:

```bash
find /mnt/lustre/<your-urika-username>/blpaper/xmls -name "*.xml" > files.txt
```

Suppose you want to run a query over all the newspapers in the folder `0000164- The Courier and Argus/`. You can create a file with the paths to these newspapers files as follows:

* On a local machine:

```bash
find "<NEWSPAPERS>/xmls/0000164- The Courier and Argus/" -name "*.xml" > files.txt
```

* On Urika:

```bash
find "/mnt/lustre/<your-urika-username>/blpaper/xmls/0000164- The Courier and Argus/" -name "*.xml" > files.txt
```