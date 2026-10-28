import Foundation
import Speech
// usage: stt <locale> <file.mp3>...   prints "<file>\t<transcript>" per file
let job = (try! String(contentsOfFile: NSHomeDirectory() + "/.inara-stt-job.txt", encoding: .utf8)).split(separator: "\n").map(String.init)
let locale = Locale(identifier: job[0])
FileManager.default.createFile(atPath: job[1], contents: nil)
let fh = FileHandle(forWritingAtPath: job[1])!
func emit(_ s: String) { fh.write((s + "\n").data(using: .utf8)!) }
let sem = DispatchSemaphore(value: 0)
var status = SFSpeechRecognizer.authorizationStatus()
if status == .notDetermined {
    SFSpeechRecognizer.requestAuthorization { s in status = s; sem.signal() }
    sem.wait()
}
guard status == .authorized else { emit("NOT AUTHORIZED: \(status.rawValue)"); exit(2) }
guard let rec = SFSpeechRecognizer(locale: locale), rec.isAvailable else { emit("recognizer unavailable"); exit(3) }
for path in job.dropFirst(2) where !path.isEmpty {
    let req = SFSpeechURLRecognitionRequest(url: URL(fileURLWithPath: path))
    req.shouldReportPartialResults = false
    req.addsPunctuation = true
    var out = ""
    let done = DispatchSemaphore(value: 0)
    rec.recognitionTask(with: req) { result, error in
        if let r = result, r.isFinal { out = r.bestTranscription.formattedString; done.signal() }
        else if let e = error { out = "ERROR: \(e.localizedDescription)"; done.signal() }
    }
    while done.wait(timeout: .now() + 0.1) == .timedOut { RunLoop.current.run(until: Date().addingTimeInterval(0.1)) }
    emit("\((path as NSString).lastPathComponent)\t\(out)")
}
emit("DONE")
